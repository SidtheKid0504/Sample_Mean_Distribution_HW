import pandas as pd
import random 
import statistics as sts
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv('./hwFiles/data/medium_data.csv')
data = df["reading_time"].tolist()

population_mean = sts.mean(data)
population_stdev = sts.stdev(data)

print("Population Mean: " + str(population_mean))
print("Population Standard Deviation: " + str(population_stdev))

dist_figure = ff.create_distplot([data], ["Population Data"], show_hist=False)

def get_sample_data_mean(counter, data):
    sample_data_points = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        random_data_point = data[random_index]

        sample_data_points.append(random_data_point)

    sample_mean = sts.mean(sample_data_points)

    return sample_mean

def show_mean_figures(mean_list):
    sample_distribution_mean = sts.mean(mean_list)
    sample_distribution_stdev = sts.stdev(mean_list)
    print ("Sampling Distribution Mean: " + str(sample_distribution_mean))
    print ("Sampling Distribution Standard Deviation: " + str(sample_distribution_stdev))
    figure = ff.create_distplot([mean_list], ["Results"], show_hist=False)
    figure.add_trace(go.Scatter(x=[sample_distribution_mean, sample_distribution_mean], y=[0, 1], mode="lines", name="Mean of Sampling Distribution"))
    figure.show()

def get_mean_of_all_samples(counter):
    final_samples_mean_result = []

    for i in range(0, counter):
        sample_mean = get_sample_data_mean(30, data)
        final_samples_mean_result.append(sample_mean)
    
    show_mean_figures(final_samples_mean_result)

dist_figure.show()
get_mean_of_all_samples(100)