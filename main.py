from strat_random_portfolio_returns import RandomPortfolioReturnStrategy

'''-----Set your initial starting paramaters below-----'''

historic_data_points = 720
benchmark_ticker = '^FTSE'
benchmark_constituents = 100
no_of_rand_portfolios = 20

'''-----Set your initial starting paramaters above-----'''

print "\n*** Random Portfolio vs Benchmark Returns Strategy ***\n"
print ">> Starting with following paramaters:"
print "Historical days:\t\t", historic_data_points
print "Benchmark ticker:\t\t", benchmark_ticker
print "Constituent count:\t\t", benchmark_constituents
print "No. of portfolios to generate:\t", no_of_rand_portfolios

strat = RandomPortfolioReturnStrategy(historic_data_points, benchmark_ticker, benchmark_constituents, no_of_rand_portfolios)
run_time = strat.run_simulation()
print "\n*** Simulation Finished (run time: %.2f" % run_time + " seconds) ***"