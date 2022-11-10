#include <complex>
#include <random>
#include <iostream>

double error(
	const std::vector<std::complex<double>>& x,
	const std::vector<std::complex<double>>& y
		)
{
	size_t N = x.size();
	double err = 0;
	for (size_t n = 0; n!= N; n++)
		err += std::abs(x[n] - y[n]);
	err /= N;
	return err;
}

std::vector<std::complex<double>> conj(
		const std::vector<std::complex<double>>& x
		)
{
	auto y = x;
	for (auto& val : y)
		val = std::conj(val);
	
	return y;	
}


std::vector<std::complex<double>> dft(
		const std::vector<std::complex<double>>& x
		)
{
	size_t N = x.size();
	std::vector<std::complex<double>> y(N, 0);
	for (size_t k = 0; k != N; k++)
		for (size_t n = 0; n!= N; n++)
			y[k] += x[n] * std::exp(-std::complex<double>(0, 1) * std::complex<double>(2 * M_PI * k * n / N, 0));
	return y;
}

std::vector<std::complex<double>> idft(
		const std::vector<std::complex<double>>& x
		)
{
	auto y = conj(dft(conj(x)));
	auto N = x.size();
	for (size_t n = 0; n != N; n++)
		y[n] /= N;
	return y;
}

int main ( int argc, char** argv)
{
	//get x
	size_t N = 1024;
	std::vector<std::complex<double>> x(N);
	std::default_random_engine generator;
	std::uniform_real_distribution<double> distribution(0, 1);
	for (size_t n = 0; n!= N; n++)
		x[n] = {distribution(generator), distribution(generator)};
	// dft and idft
	auto y = dft(x);
	auto x1 = idft(y);
	double err = error(x, x1);
	std::cout << "Error = " << err << '\n';

	return 0;
}


