from pandasql import sqldf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

result = pd.read_csv('clean_data.csv')
mclass_total = result[result['mclass_lvl'].notna()]
txkea_total = result[result['txkea_level'].notna()]
demo = pd.read_csv('DEMO.csv')
mclass = pd.read_csv('MCLASS.csv')
txkea = pd.read_csv('TXKEA.csv')


def numberof_students():
    mclass_total = result[result['mclass_lvl'].notna()]
    txkea_total = result[result['txkea_level'].notna()]
    return print("There were " + str(len(mclass_total)) + " students that took the mclass assessment and " + str(len(txkea_total)) +\
                    " students that took the txtea assessment.")

def assessment_specifier():
    eco = result[result['eco'] == 'YES']
    eco_mclass = eco[eco['mclass_lvl'].notna()]
    eco_txkea = eco[eco['txkea_level'].notna()]
    el = result[result['el'] == 'YES']
    el_mclass = el[el['mclass_lvl'].notna()]
    el_txkea = el[el['txkea_level'].notna()]
    sped = result[result['spec_ed'] == 'YES']
    sped_mclass =sped[sped['mclass_lvl'].notna()]
    sped_txkea = sped[sped['txkea_level'].notna()]
    graph = pd.DataFrame(
        { "mclass" : [len(sped_mclass), \
                      len(el_mclass), len(eco_mclass)],
                      "txkea" : [len(sped_txkea), len(el_txkea), \
                                   len(eco_txkea)]}, \
                                    index = ['sped', 'el', 'eco'])
    return graph

def graph_specifier():
    identifier = ("Spec_ed", "English_learner", "Eco_dis")
    proportion = {
    'mclass': (7.3, 13.9, 59.4),
    'txkea': (7.6, 12.6, 59.3),
}
    x = np.arange(len(identifier))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in proportion.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('percentage')
    ax.set_title('Proportion of students with given specifier')
    ax.set_xticks(x + .125, identifier)
    ax.legend()

    return plt.show()

def ethnicity_count():
    cnt = 0
  
# list to hold visited values
    visited = []
  
# loop for counting the unique
# values in height
    for i in range(0, len(result['ethnicity'])):
    
        if result['ethnicity'][i] not in visited: 
        
            visited.append(result['ethnicity'][i])
          
            cnt += 1
    eth_mclass = []
    for i in visited:
        count = len(mclass_total[mclass_total['ethnicity'] == i])
        eth_mclass.append(count)
    eth_txkea = []
    for i in visited:
        count = len(txkea_total[txkea_total['ethnicity'] == i])
        eth_txkea.append(count)
    ethnicity_graph = pd.DataFrame({ "mclass" : eth_mclass,
    "txkea" : eth_txkea}, index = [visited])
    ethnicity_graph.mclass = round(ethnicity_graph.mclass/len(mclass), 3) * 100
    ethnicity_graph.txkea = round(ethnicity_graph.txkea/len(txkea), 3) * 100
    return ethnicity_graph

def ethnicity_graph():
    ethnicity_graph = ethnicity_count()
    identifier = ('White',
    'Black',
    'Two or more',
    'Hispanic/Latino',
    'Indigenous',
    'Asian',
    'Pacific')
    proportion = {
        'mclass': ethnicity_graph.mclass,
        'txkea': ethnicity_graph.txkea,
        }

    x = np.arange(len(identifier))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = -.5

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in proportion.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
  
        multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('percentage')
    ax.set_title('Proportion of students with given specifier')
    ax.legend()
    ax.set_xticks([0,1,2,3,4,5,6])
# Set the tick labels
    ax.set_xticklabels(identifier)
    plt.xticks(rotation = 60)
    return plt.show()