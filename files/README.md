# P6 
## Task: Try modifying the structure of the new layers that were added on top of ResNet20.
For this task, a new layer was added at the end of the original network. 
The last layer of the original network was modified to get input 64 nodes and output 30 nodes, and a new output layer was added after that to get input 30 nodes and output 10 nodes. 
Also, the code was modified so that it could run on GPU. 

On training both the original model and the modified model, the losses were compared over epochs and plotted:

![alt text](compare.jpg)
Fig: Running loss over epochs for original and modified model 

While both the models seemed to have reached a similar state by the end of the training, a closer look at loss values shows that the modified model worked slightly better that the original model.
Final loss value for:
- Original model: 1.001
- Modified model: 0.989
