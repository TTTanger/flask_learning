# Notebook

### What are the major steps in system development?

##### 1. Requirement engineering

**Object: Figure out what we want to achieved**
***What is requirement?***

1. A list of items
2. Schedule (time involved)
3. What is wanted (from both sides, agreement)

##### 2. Software design

**Object: Cutting down the big tasks into smaller ones that can run independently.**

##### 3. Implementation

**Object: The coding itself.**

##### 4. Validation

**Object: Check whether it meets the requirements.**

___

#### Requirement engineering (Most critical in Software Engineering)

##### Techniques

1. Documentation
2. Interview

- Boss
- Employees

3. Participating observation	

##### Sideconditions

1. Commercial
2. Emotional
3. Political
4. Mental (Tacit knowoledge)

##### What are the possible techniques for to figure out what is needed (Requirement engineering)?

1. Check documentation

- Job description 
- Protocols of meetings
- Process descriptions

2. Interviews of stakeholders 
3. Participating observation (become part of the system)

##### What are the challenges of Requirement engineering?

1. Commercial Challenge
   ->Time of stakeholders (employees) is needed: put the needed time of the employees into contract.

2. Emotional challenge
   ->People may be disturbed from whatever: get specialists.

3. Political challenge
   ->Second agendas can be discovered by cross checking (asking colleagues).
4. Mental (tacit knowledge)
   ->Only chance is participating observation.

##### What aspects define the quality of a requirement?

1. Completeness: No feature of interest is missing
2. Consistency: No two requirements contradict with each other
3. Unambiguous: Each requirement can be interpreted in only one way
4. Correctness: No unintended feature is described

___

#### Software design

##### What is the role of models of application domain? (Model of the real world)

1. It structures the heap of information we have gathered.
2. It emphasizes the important aspects.
3. It makes the information specific (Nails it down)

##### What basic type of models are we dealing with(do we use)?

1. Models of the real world (application domain).
2. Models in our system (Solution domain).

##### What are the core characteristics of a model?

A model emphasizes certain aspect and leaves aside other aspects.

##### How are these models written?

Most types of the software are written in Unified Modeling Languages (UML)

##### What types of models are important for our system?

1. Functional model: to deal with events from outside perspective 
2. Object model: the components used in the program 
3. Dynamic model: how do the components of our program interact

___

## Use-case

***1. Name***
***2. Actor***
***3. Trigger***
***4. Precondition*** 
***5. Activity***
***6. Postcondition*** 

#### How to identify a use-case?

1. What is the name of the use-case?
2. Who is the actor (can be human or technical)?
3. Is there a precondition and a postcondition to be named?
4. What makes the postcondition out of the precondition?
5. What starts the whole process (trigger)?
6. Whether there are sub use-cases under the parent use-case? 

#### Identifying relationships among actors and use-cases.

1. Drawing a use case diagram
2. Graphical elements: SWEI-PDF 3, Page 45

- A stickman represents an actor
- Bubbles represent events
- Arrows 

##### Use-cases can be inclusive or extended

1. Inclusive use-cases are necessary 
2. Extended use-cases are possible

*Decorating a dish of rice: extension of cooking rice*
*Cutting vegetables before cooking: inclusion necessary* 

___

## ✨Use-case Diagram (PDF 4)

##### 1. Dispatcher (Actor)

##### 2. FieldOfficer (Actor)

##### 3. Use-cases

___

##  ✨ Activity Diagram (Static)

##### 1. Decision node & Merge node 💠	(single process)

##### 2. Fork node & Join node ｜	(multiple process)

##### 3. Conditions[ ]

##### 4. Initial node	·

##### 5. Action node □ 

##### 6. Flow → (single) & ⇢ (multiple)

###### Objects

1. real world objects
2. class
3. instantiated objects

___

## Class Diagram (Dynamic)

#### Multiplicity

e.g. 
1..* means 1 or more
0..* means 0 or more

![](Notebook/IMG_0712%202.png)

![](Notebook/IMG_0713.png)


#### Composite

Diamond node to show a strong inclusion relationship

##### What is the difference between a decision node and a merge node on the one hand and fork node with a join node on the other hand?

1. The decision & merge node there is a condition
2. Fork & join node there is no condition

##### What is the difference between a decision node and a fork node not in UML?

1. Fork node works unconditionally. Results in processing.
2. Decision node works conditionally. Only one branch after it is followed.

##### What are the nodes called that get the multiple branches after a decision node or a fork node together again?

1. Decision node: merge node.
2. Fork node: join node.

___

### Some concepts

#### Object classes

*Contain preconditions and the postconditions
(model)*

#### Boundary classes

*Important for communication and interfaces
(view)*

#### Control classes

*Bring the functionality
(control)*

#### MVC model

*model, view, controller*

___

## Object diagram

___

## Sequence Diagram 