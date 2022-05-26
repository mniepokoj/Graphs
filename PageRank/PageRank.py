from collections import defaultdict
import math
import random
import numpy as np

from numpy import tensordot


class PageRank:
    @staticmethod
    def monteCarlo(adj_list: dict) -> str:
        amount = 1000000
        n = len(adj_list)+1
        d = 0.15
        temp_list = []
        for i in range(0, n):
            temp_list.append(0)

        #Glowna petla
        iter = random.randint(1, n-1)
        for i in range(0, amount):
            r = random.random()
            while r < d:
                iter = random.randint(1, n-1)
                r = random.random()
            temp_list[iter] += 1
            k = len(adj_list[iter])
            r = random.randint(0, k-1)
            iter = adj_list[iter][r]
        text = ''


        #sortowanie i wyswietlanie
        for i in range(1, len(temp_list)):
            min_iter = 1
            for k in range(1, len(temp_list)):
                if temp_list[k] !=  2:
                    min_iter = k
                    break
            for j in range(2, len(temp_list)):
                if temp_list[j] == 2:
                    continue
                if temp_list[j] > temp_list[min_iter]:
                    min_iter = j
            
            text += str(min_iter) + ": " + str(temp_list[min_iter]/(amount)) + '\n'
            temp_list[min_iter] = 2

        return text


    @staticmethod
    def power_iteration(adj_list: dict) -> str:
        n = len(adj_list)
        e = 1. / n
        d = 0.15
        P = np.zeros((n, n))
        A = np.zeros((n, n))

        #inicjacja
        for i in range(0,len(A)):
            for j in range(0, len(A[i])):
                if j+1 in adj_list[i+1]:
                    A[i][j] = 1/len(adj_list[i+1])

        for i in range(0,len(P)):
            for j in range(0, len(P[i])):
                if len(adj_list[i+1]) != 0:
                    P[j][i] = (1-d)*A[i][j] + d *e
                else:
                    P[j][i] = e*d
        p = np.zeros((n, 1))

        sum = 0
        for i in range(0, n):
            for j in range(0, n):
                sum += P[i][j]
            sum = 0

        for i in range(0, len(p)):
            p[i] = e


        #relaksacja
        delta = 1
        err = 1e-20
        text = ''
        while delta > err:
            p_new = P.dot(p)
            p_delta = p_new-p
            delta = 0
            for i in p_delta:
                delta += i*i
            p = p_new
        
        #sortowanie i wyswietlanie
        for i in range(0, len(p)):
            min_iter = 0
            for k in range(0, len(p)):
                if p[k] !=  2:
                    min_iter = k
                    break
            for j in range(1, len(p)):
                if p[j] == 2:
                    continue
                if p[j] > p[min_iter]:
                    min_iter = j
            
            text += str(min_iter+1) + ": " + str(p[min_iter]) + '\n'
            p[min_iter] = 2

        return text