import math
import numpy as np

class GA:
    class Chromosome():
        def __init__(self, genes_len = 10, min=-5, max=5, genes = []):
            if len(genes) == 0:
                self.__genes = np.random.uniform(min, max, genes_len)
            else:
                self.__genes = genes

        def mutate(self, min, max):
            mutate_num = np.random.randint(0, len(self.__genes)-1, 1)
            mutate_index = np.random.randint(0, len(self.__genes)-1, mutate_num)
            new_chr = np.array(self.__genes)
            for index in mutate_index:
                new_chr[index] = np.random.uniform(min, max, 1)
            return GA.Chromosome(genes=new_chr)

        def crossOver(self, other):
            cop = np.random.randint(0, len(self.__genes), 2)
            chr1 = np.array(self.__genes)
            chr2 = np.array(other.getGenes())
            chr1[cop[0]: cop[1]], chr2[cop[0]: cop[1]] = chr2[cop[0]: cop[1]], chr1[cop[0]: cop[1]]
            chr1[cop[0]: cop[1]] = [(x+y)/2 for x,y in zip(chr1[cop[0]: cop[1]], chr2[cop[0]: cop[1]])]
            chr2[cop[0]: cop[1]] = chr1[cop[0]: cop[1]]
            return list([GA.Chromosome(genes=chr1), GA.Chromosome(genes=chr2)])

        def getGenes(self):
            return list(self.__genes).copy()

    def __init__(self, chr_size):
        self.__chr_size = chr_size
        self.__population = []
        self.__top = {"cost_value": float('Inf'), "chr": []}


    def genPopulation(self,  max, min, pop_size):
        for p in range(pop_size):
            self.__population.append(self.Chromosome(self.__chr_size, min, max))
        return self.__population

    def mutuation(self, num, min, max):
        if num > len(self.__population):
            raise ("number of mutation is higher than population")
        mutated = []
        mutate_indexs = np.random.randint(0, len(self.__population), num)
        for mutate_index in mutate_indexs:
            mutated = mutated + [self.__population[mutate_index].mutate(min, max)]
        return mutated

    def crossOver(self, num):
        crossover_pop = []
        for i in range(num):
            s = list(np.random.randint(0, len(self.__population), 2))
            crossover_pop = crossover_pop + self.__population[s[0]].crossOver(self.__population[s[1]])
        return crossover_pop

    def calFitness(self, func, pop = []):
        if(len(pop)==0):
            fitness_list = [func(chr.getGenes()) for chr in self.__population]
        else:
            fitness_list = [func(chr.getGenes()) for chr in pop]
        sorted_list = sorted(zip(fitness_list, self.__population),key=lambda f:f[0])
        sorted_chromosome = [s[1] for s in sorted_list]
        top_fitness = sorted_list[0][0]
        print(top_fitness)
        if(self.__top["cost_value"] > top_fitness ):
            self.__top["cost_value"] = top_fitness
            self.__top["chr"] = sorted_list[0][1]
        return sorted_chromosome, top_fitness
