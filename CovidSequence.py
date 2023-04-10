#!/usr/bin/env python
# coding: utf-8

# In[5]:


wuhan = list(open("wuhan-1_NC_045512.2.txt").read())
alpha = list(open("alpha_OK104629.1.txt").read())
beta = list(open("beta_OU205079.txt").read())
data_list_1 = [wuhan, alpha]
data_list_2 = [wuhan, beta]
data_list_3 = [alpha, beta]
# print(len(wuhan))
# print(len(alpha1))
# print(len(alpha2))

# for data in data_list:
#     if len(data) != 29903:
        


def two_seq_compare(data_list):
    genome = []
    diff_genome = []
    diff_place = []
    max_val = len(data_list[0])

    for i in range(max_val):
        genome.append({i+1:[]})
        for data in data_list:
            genome[i][i+1].append(data[i])
        first = genome[i][i+1][0]
        for lett in genome[i][i+1]:
            if lett != first and lett != "N":
                diff_place.append(i)
                diff_genome.append(genome[i])

    print(1-(len(diff_place)/max_val))
    return diff_genome 
    

def two_seq_avg_genome(data_list):
    avg_genome = []
    max_val = len(data_list[0])
    
    for i in range(max_val):
        avg_genome.append({i+1:[]})
        for data in data_list:
            avg_genome[i][i+1].append(data[i])
        first = avg_genome[i][i+1][0]
        for lett in avg_genome[i][i+1]:
            if lett != first and lett != "N":
                avg_genome.remove(avg_genome[i])
                avg_genome.append("N")
            else:
                avg_genome.remove(avg_genome[i])
                avg_genome.append(lett)
                break

    var = "".join(avg_genome)

    print(len(var))
    with open('average_genome.txt', "w") as file:
        file.write(var)
        file.close()
    
two_seq_compare(data_list_1)
two_seq_avg_genome(data_list_1)


# In[ ]:




