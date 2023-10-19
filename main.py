
class NeuralNetworkMCP():

    def __init__(self,neurons:list[float],W0:float,T:float) -> None:
        self.neurons = neurons
        self.W0 = W0
        self.T = T
    
    def learn(self,input_list:list[tuple],e_output_list:list[int])->list[int]:
        sum = 0
        data_counter = 0
        o_output_list = []
        for expected_answer in e_output_list: # For every set of inputs and expected output:
            sum = self.W0
            for counter in range(len(input_list[data_counter])): # For every input in the set of inputs:
                
                i = input_list[data_counter][counter]
                w = self.neurons[counter]
                sum += i*w
                
            
            if sum>=self.T: # If the answer is greater than the threshold: 
                sum = self.T # Make the answer the threshold
            
            if sum == expected_answer: # If answer is same as the expected:
                delta = 0 # Don't change anything
            else: # Otherwise change everything by the delta
                delta = expected_answer - sum
            self.W0 += delta
            for counter in range(len(self.neurons)): # For every neuron
                if input_list[data_counter][counter] >= 1: # If the input was activated, reinforce it by the delta
                    self.neurons[counter] += delta
            o_output_list.append(sum)
            data_counter+=1
        return(o_output_list)


mcpOR = NeuralNetworkMCP([0,0],0,1)

trainingData = [[(0,0),(0,1),(1,0),(1,1)],
                [0,1,1,1]
                ]

Results = mcpOR.learn(trainingData[0],trainingData[1])
print(f"W0:{mcpOR.W0}, Neurons: {mcpOR.neurons} ")
while Results != trainingData[1]:
    Results = mcpOR.learn(trainingData[0],trainingData[1])
    print(f"W0:{mcpOR.W0}, Neurons: {mcpOR.neurons} ")
print(f"W0:{mcpOR.W0}, Neurons: {mcpOR.neurons} ")
