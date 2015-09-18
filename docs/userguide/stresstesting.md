# Stress Testing the Hex

create a file /tmp/stress.yml on your master node
```
- hosts: host                                                                                                                                                                                          
  sudo: yes                                                                                                                                                                                            
  tasks:                                                                                                                                                                                               
    - name: install stress                                                                                                                                                                             
      apt: name=stress state=latest                                                                                                                                                                    
                                                                                                                                                                                                       
    - name: run stress                                                                                                                                                                                 
      shell: stress --cpu 8 --io 4 --vm 2 --vm-bytes 2G -d 10 --hdd-bytes 10G --timeout 5m  
```

run ```ansible-playbook /tmp/stress.yml``` to start stressing the system