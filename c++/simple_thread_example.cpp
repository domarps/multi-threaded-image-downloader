#include <iostream>
#include <cmath>
#include <sstream>
#include <thread>
#include <chrono>
#include <ctime>
#include <mutex>

int GetRandom(int max)
{
  srand(time(NULL));
  return rand() % max;
}

void ExecuteThread(int id)
{
  auto nowTime = std::chrono::system_clock::now();
  std::time_t sleepTime = 
    std::chrono::system_clock::to_time_t(nowTime);
  tm myLocalTime = *localtime(&sleepTime);

  std::cout << "Thread " << id << " Sleep time : " << std::ctime(&sleepTime) << "\n";

  //thread -> block of code that executes
  std::this_thread::sleep_for(std::chrono::seconds(GetRandom(3)));
  nowTime = std::chrono::system_clock::now();
  sleepTime = std::chrono::system_clock::to_time_t(nowTime);
  std::cout << "Thread " << id << " Awake time : " << std::ctime(&sleepTime) << "\n";
}
int main() 
{
  std::thread th1(ExecuteThread, 1);
  th1.join(); //main waits for this thread to stop executing before executing the remaining piece of code
  std::thread th2(ExecuteThread, 2);
  th2.join();
  return 0;
}
