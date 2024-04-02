
# Automania

## Context:
In the realm of virtual robotics, a simulator exists, replicating the conditions and challenges faced by exploratory rovers in distant, alien terrains. Participants will delve into the core of robotic operations, including perception, decision-making, and actuation, within this simulated environment.

## Challenge Statement:
Participants are invited to enter the domain of autonomous exploration, leveraging a virtual environment modeled after celestial exploration challenges. Your mission is to enhance an autonomous rover's ability to navigate, analyze, and map its surroundings effectively. This endeavor will be executed within a sophisticated simulation, designed to mimic the uncharted landscapes of a distant world.

## Requirements:
- Develop or refine the autonomous navigation system for a virtual rover.
- Utilize a provided simulator to test and demonstrate the rover's capabilities.
- Implement and improve algorithms for environmental perception, decision-making, and actuation.
- Conduct data analysis and mapping of the virtual terrain, leveraging provided tools and datasets.
- Optimize the rover's performance within the simulator, ensuring efficient and accurate exploration.

## Tools and Resources:
- A simulator built on the Unity game engine, accessible for various operating systems.

## Project Phases:
1. **Data Collection:** Maneuver the rover within the simulator's "Training Mode" to gather environmental data.
2. **Analysis and Mapping:** Analyze collected data to construct a comprehensive map of the virtual terrain.
3. **Autonomous Navigation:** Develop and refine the rover's ability to traverse the simulation autonomously, making intelligent decisions based on environmental analysis.

## Detailed Instructions:

1. **Fill in the Blanks:**
   Within each script, there are blank spaces that require suitable variable names or values. Your task is to identify these blank spaces and populate them accordingly.

2. **Implement Missing Logic:**
   Certain sections of logic within the scripts are commented out. These sections need to be implemented based on the provided comments. It is essential to carefully understand the logic requirements and ensure accurate implementation.

## Additional Guidelines:

- Pay close attention to the provided comments within each script, as they offer valuable insights into the required modifications.
- Test your modified scripts thoroughly to ensure they function correctly within the Unity environment.
- Feel free to optimize the code wherever possible to improve performance and maintainability.

## Outcome:
The ultimate objective is to significantly enhance the rover's autonomous navigation capabilities, demonstrating proficiency in robotic principles and the application of algorithms in dynamic and uncertain environments. Your efforts will culminate in a presentation showcasing the rover's improved operational efficacy, detailed analysis of the implemented methodologies, and a reflection on the simulation settings' impact on performance.

Participants are encouraged to explore beyond the boundaries of conventional approaches, employing innovative techniques and strategies to address the complexities of autonomous extraterrestrial exploration.

  

## The Simulator
The first step is to download the simulator build that's appropriate for your operating system.  Here are the links for [Linux](https://s3-us-west-1.amazonaws.com/udacity-robotics/Rover+Unity+Sims/Linux_Roversim.zip), [Mac](	https://s3-us-west-1.amazonaws.com/udacity-robotics/Rover+Unity+Sims/Mac_Roversim.zip), or [Windows](https://s3-us-west-1.amazonaws.com/udacity-robotics/Rover+Unity+Sims/Windows_Roversim.zip).  

You can test out the simulator by opening it up and choosing "Training Mode".  Use the mouse or keyboard to navigate around the environment and see how it looks.

## Dependencies
You'll need Python 3 and Jupyter Notebooks installed to do this project.  The best way to get setup with these if you are not already is to use Anaconda following along with the [RoboND-Python-Starterkit](https://github.com/ryan-keenan/RoboND-Python-Starterkit). 


Here is a great link for learning more about [Anaconda and Jupyter Notebooks](https://classroom.udacity.com/courses/ud1111)

## Recording Data
I've saved some test data for you in the folder called `test_dataset`.  In that folder you'll find a csv file with the output data for steering, throttle position etc. and the pathnames to the images recorded in each run.  I've also saved a few images in the folder called `calibration_images` to do some of the initial calibration steps with.  

The first step of this project is to record data on your own.  To do this, you should first create a new folder to store the image data in.  Then launch the simulator and choose "Training Mode" then hit "r".  Navigate to the directory you want to store data in, select it, and then drive around collecting data.  Hit "r" again to stop data collection.

## Data Analysis
Included in the IPython notebook called `Rover_Project_Test_Notebook.ipynb` are the functions from the lesson for performing the various steps of this project.  The notebook should function as is without need for modification at this point.  To see what's in the notebook and execute the code there, start the jupyter notebook server at the command line like this:

```sh
jupyter notebook
```

This command will bring up a browser window in the current directory where you can navigate to wherever `Rover_Project_Test_Notebook.ipynb` is and select it.  Run the cells in the notebook from top to bottom to see the various data analysis steps.  

The last two cells in the notebook are for running the analysis on a folder of test images to create a map of the simulator environment and write the output to a video.  These cells should run as-is and save a video called `test_mapping.mp4` to the `output` folder.  This should give you an idea of how to go about modifying the `process_image()` function to perform mapping on your data.  

## Navigating Autonomously
The file called `drive_rover.py` is what you will use to navigate the environment in autonomous mode.  This script calls functions from within `perception.py` and `decision.py`.  The functions defined in the IPython notebook are all included in`perception.py`. You are provided with a partial implementation of the some of the scripts. Your task is to modify the script according to the instructions provided below.

`drive_rover.py` should work as is if you have all the required Python packages installed. Call it at the command line like this: 

```sh
python drive_rover.py
```  

Then launch the simulator and choose "Autonomous Mode".  The rover should drive itself now! 

**Note: running the simulator with different choices of resolution and graphics quality may produce different results!  Make a note of your simulator settings in your writeup when you submit the project.**




