#
#
#
#
**Network automation using REST API with Jenkins CI/CD tool** 






1. ## **Introduction**


1. ### **Overview**
Provide description about my network automation with Jenkins project 

1. **SYSTEM OVERVIEW**

Automate the process of configuration network devices using python programing language providing two way to send configuration to network devices by ( SSH or REST API ) and then using Jenkins to  inherent my project the CI/CD philosophy. , asking the user to choose the routing protocol ( OSPF , BGP) or add static route and edit the configuration in yaml file. 

1. ## **System Architecture**

1. ### **Architectural Design**

- Overview of CI/CD of my project


![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.001.png)













- ` `The network of the connected devices in my host environment


![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.002.png)


1. ### **Flow chart Description**
Flow chart of the code to automat the configuration of network device.

![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.003.png)















1. ## **CODE  Details**


1. ### **Data Description**

![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.004.png)
1. ### **Code Description and snippets**
Take the choice of ospf protocol to describe the steps of the code

- ospf.yaml file

  ![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.005.png)






- ospf.j2 file 

  the jinja part to make configuration suitable for ssh commands

  ![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.006.png)

- the jinja part to make configuration 
- suitable for yangmodel

`	`![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.007.png)













- the output of rendering in case of rest api

 

  ![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.008.png)

- the output of rendering in case of  SSH

  ![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.009.png)










1. ## **Running my project as a container**

- My Dockerfile

  ![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.010.png)


- Building image

  ![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.011.png)

- Create in Docker ipvlan Network 

  ![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.012.png)

- Run a container of my project

  ![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.013.png)









- Showing running 

  ![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.014.png)





1. ## **Jenkins Pipeline**

The steps of the pipeline 

![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.015.png)




- In the stage of testing running all the combination of possible input

  (bgp,ospf,static)--à(ssh,rest api) that give us 6 possibilities:

  The output of this stage is in log file : [log.txt](https://github.com/Omar-Ahmed97/Network-automation-Project/blob/master/log.txt) 

.![](Aspose.Words.de79f159-d745-454b-a8a2-7e2e98e8ea10.016.png)

