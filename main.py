from strat_random_portfolio_returns import RandomPortfolioReturnStrategy

'''-----Set your initial starting parameters below-----'''

historic_data_points = 720
benchmark_ticker = '^FTSE'
benchmark_constituents = 100
no_of_rand_portfolios = 40
filter_stock_country = 'United Kingdom'

'''-----Set your initial starting parameters above-----'''

print "\n*** Random Portfolio vs Benchmark Returns Strategy ***\n"
print ">> Starting with following parameters:"
print "Historical days:\t\t", historic_data_points
print "Benchmark ticker:\t\t", benchmark_ticker
print "Constituent count:\t\t", benchmark_constituents
print "No. of portfolios to generate:\t", no_of_rand_portfolios

if filter_stock_country:
		print "Filtering stocks on country:\t", filter_stock_country

strat = RandomPortfolioReturnStrategy(historic_data_points, benchmark_ticker, benchmark_constituents, no_of_rand_portfolios, filter_stock_country)
run_time = strat.run_simulation()
print "\n*** Simulation Finished (run time: %.2f" % run_time + " seconds) ***"