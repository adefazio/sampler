#include <random>
#include <iostream>

std::random_device rd;
std::mt19937 mt(rd());
std::uniform_real_distribution<double> dist(0.0,1.0);

double uniform_fast() {
  return dist(mt);
}
