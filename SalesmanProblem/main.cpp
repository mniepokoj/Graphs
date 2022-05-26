#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
#include <string>

void readData(const std::string& file, std::vector<std::pair<float, float>>& data)
{
	std::ifstream f;
	f.open(file);
	if (f.good())
	{
		int a, b;
		while (!f.eof())
		{
			f >> a;
			f >> b;
			data.push_back(std::pair<float, float>(a, b));
		}
	}
}

float distance(const std::pair<float, float>& p1, const std::pair<float, float>& p2)
{
	float a = p1.first - p2.first;
	float b = p1.second - p2.second;
	return std::sqrt(a*a + b*b);
}

float frand()
{
	return (float(rand()) / float((RAND_MAX)));
}

inline float checkUnique(int a, int b, int c, int d)
{
	return (a == b || a == c || a == d || b == c || b == d || c == d);
}

float calculateDistance(int start, int end, const std::vector<int>& path, const std::vector<std::pair<float,float>>& data)
{
	float sum = 0;

	for (int i = start; i < end; i++)
	{
		sum += distance(data[path[i]], data[path[i+1]]);
	}
	return sum;
}


void saveData(	const std::vector<int>& path_old, const std::vector<int>& path_new, 
				const std::vector<std::pair<float, float>>& data)
{
	std::ofstream f;
	std::string s;

	f.open("startPath.dat", std::ios_base::trunc);
	for (const auto& i : path_old)
	{
		f << data[i].first << ' ' << data[i].second << '\n';
	}
	f.close();

	f.open("finalPath.dat", std::ios_base::trunc);
	for (const auto& i : path_new)
	{
		f << data[i].first << ' ' << data[i].second << '\n';
	}
	f.close();
}


int main()
{

	constexpr int MAX_IT = 1000;
	constexpr int OUTSIDE_LOOP_IT = 100;
	constexpr int TEMPERATURE_LOOP = 34;
	constexpr float cooling_parameter = 2.5f;


	srand(time(NULL));



	std::vector<std::pair<float, float>> data;
	readData("input_150.dat", data);


	float len = 0;
	float len_min = FLT_MAX;

	std::vector<int> shortest_path;
	std::vector<int> first_path;

	std::vector<int> path;
	for (int i = 0; i < data.size() - 1; i++)
	{
		path.push_back(i);
	}
	path.push_back(0);
	shortest_path.assign(path.begin(), path.end());
	first_path.assign(path.begin(), path.end());

	for(int i = 0; i <= OUTSIDE_LOOP_IT; i++)
	{
		len = 0;
		for (int i = TEMPERATURE_LOOP; i >= 1; i--)
		{
			float T = 0.001f * std::pow(i, cooling_parameter);
			for (int it = 0; it < MAX_IT; it++)
			{
				int a, b, c, d;
				do
				{
					a = rand() % (path.size() - 3);
					b = a + 1;
					c = rand() % (path.size() - b - 2) + b + 1;
					d = c + 1;
				} while (a == c || checkUnique(path[a], path[b], path[c], path[d]));

				float distance_old = calculateDistance(a, d, path, data);

				std::reverse(path.begin() + b, path.begin() + c);
				float distance_new = calculateDistance(a, d, path, data);

				if (distance_old < distance_new && frand() > exp(-(distance_new - distance_old) / T))
				{
					std::reverse(path.begin() + b, path.begin() + c);
				}
			}
		}
		for (int i = 0; i < path.size() - 1; i++)
		{
			len += distance(data[path[i]], data[path[i + 1]]);
		}

		if (len < len_min)
		{
			len_min = len;
			std::memcpy(shortest_path.data(), path.data(), sizeof path.data() * path.size());
		}
	}

	std::cout << "Minimalna poczatkowa wynosi: " << calculateDistance(0, first_path.size() - 1, first_path, data) << std::endl;
	std::cout << "Minimalna poczatkowa wynosi: " << calculateDistance(0, shortest_path.size() - 1, shortest_path, data) << std::endl;
	saveData(first_path, shortest_path, data);
	std::cout << "Sciezki zostaly zapisane do plikow startPath.dat oraz finalPath.dat " << std::endl;
	std::cout << "Aby otrzymac rozwiazanie graficzne nalezy wpisac w konsoli './plot.plt': "<< std::endl;
	return 0;
}
