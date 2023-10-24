// This program demonstrates how to create a pipeline scheduling framework
// that propagates a series of integers and adds one to the result at each
// stage.
//
// The pipeline has the following structure:
//
// o -> o -> o
// |         |
// v         v
// o -> o -> o
// |         |
// v         v
// o -> o -> o
// |         |
// v         v
// o -> o -> o

#include <taskflow/taskflow.hpp>
#include <taskflow/algorithm/pipeline.hpp>
void run_script(const std::string& scriptPath) {
  std::cout << "Running script: " << scriptPath << "\n";

  std::string command = "cd /ChipPilot/sh && bash " + scriptPath;
  int exitCode = std::system(command.c_str());

  if (exitCode == 0) {
    std::cout << "Script: " << scriptPath << " execution completed.\n";
  } else {
    std::cerr << "Script execution failed with exit code: " << exitCode << "\n";
  }
}
int main() {

  tf::Taskflow taskflow("pipeline");
  tf::Executor executor(1);

  const size_t num_lines = 2;

  // custom data storage
  std::array<size_t, num_lines> buffer;

  // the pipeline consists of three pipes (serial-parallel-serial)
  // and up to four concurrent scheduling tokens
  tf::Pipeline pl(num_lines,
    tf::Pipe{tf::PipeType::SERIAL, [&buffer](tf::Pipeflow& pf) {
      if(pf.token() == 1) {
        pf.stop();
      }
      // save the result of this pipe into the buffer
      else {
        run_script("/ChipPilot/sh/iFP_gcd.sh");
      }
    }},

    tf::Pipe{tf::PipeType::SERIAL, [&buffer](tf::Pipeflow& pf) {
      if(pf.token() == 1) {
        pf.stop();
      }
      // save the result of this pipe into the buffer
      else {
        run_script("/ChipPilot/sh/iNO_fix_fanout_gcd.sh");
      }
    }},

    tf::Pipe{tf::PipeType::SERIAL, [&buffer](tf::Pipeflow& pf) {
      if(pf.token() == 1) {
        pf.stop();
      }
      // save the result of this pipe into the buffer
      else {
        run_script("/ChipPilot/sh/iPL_gcd.sh");
      }
    }},
    // tf::Pipe{tf::PipeType::SERIAL, [&buffer](tf::Pipeflow& pf) {
    //   if(pf.token() == 1) {
    //     pf.stop();
    //   }
    //   // save the result of this pipe into the buffer
    //   else {
    //     run_script("/ChipPilot/sh/iPL_eval_gcd.sh");
    //   }
    // }},
    tf::Pipe{tf::PipeType::SERIAL, [&buffer](tf::Pipeflow& pf) {
      if(pf.token() == 1) {
        pf.stop();
      }
      // save the result of this pipe into the buffer
      else {
        run_script("/ChipPilot/sh/iCTS_gcd.sh");
      }
    }},
    // tf::Pipe{tf::PipeType::SERIAL, [&buffer](tf::Pipeflow& pf) {
    //   if(pf.token() == 1) {
    //     pf.stop();
    //   }
    //   // save the result of this pipe into the buffer
    //   else {
    //     run_script("/ChipPilot/sh/iCTS_eval_gcd.sh");
    //   }
    // }},
    tf::Pipe{tf::PipeType::SERIAL, [&buffer](tf::Pipeflow& pf) {
      if(pf.token() == 1) {
        pf.stop();
      }
      // save the result of this pipe into the buffer
      else {
        run_script("/ChipPilot/sh/iCTS_STA_gcd.sh");
      }
    }}
  );

  // build the pipeline graph using composition
  tf::Task init = taskflow.emplace([](){ std::cout << "ready\n"; })
                          .name("starting pipeline");
  tf::Task task = taskflow.composed_of(pl)
                          .name("pipeline");
  tf::Task stop = taskflow.emplace([](){ std::cout << "stopped\n"; })
                          .name("pipeline stopped");

  // create task dependency
  init.precede(task);
  task.precede(stop);

  // dump the pipeline graph structure (with composition)
  taskflow.dump(std::cout);

  // run the pipeline
  executor.run(taskflow).wait();

  return 0;
}
