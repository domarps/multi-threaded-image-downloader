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

std::string GetTime()
{
  auto nowTime = std::chrono::system_clock::now();
  std::time_t sleepTime = std::chrono::system_clock::to_time_t(nowTime);
  return std::ctime(&sleepTime); 
}


double accountBalance = 1000;

//protect shared data from being accessed at the time
std::mutex acctLock;

void GetMoney(int id, double withdrawalAmount)
{
  std::lock_guard<std::mutex> lock(acctLock);
  std::this_thread::sleep_for(std::chrono::seconds(3));
  
  std::cout << id << " tries to withdraw $" 
            << withdrawalAmount << " on " << GetTime() << "\n";
  
  if(accountBalance - withdrawalAmount >= 0)
  {
    accountBalance -= withdrawalAmount;
    std::cout << "New account balance is " << accountBalance << "\n";
  }
  else
  {
    std::cout << "not enough account " << "\n";
  }
  /*
  acctLock.lock();
  WRAPPING CODE HERE IS NOT SAFE IF AN EXCEPTION WERE TO OCCUR
  acctLock.unlock();
  */
}
int main()
{
  std::thread threads[10];

  for(int i = 0; i < 10; i++)
  {
    threads[i] = std::thread(GetMoney, i, 15);
  }
  for(int i = 0; i < 10; i++)
  {
    threads[i].join();
  }

}
