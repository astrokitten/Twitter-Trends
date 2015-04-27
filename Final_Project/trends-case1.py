#Brooke Bullek & Daniel Vasquez
#Final Project; CSCI 203; Prof. Shalan
#Phase 2: Visualize Results Using VPython

""" Uses VPython to demonstrate average sentiment and raw frequency of tweets, given a
    user-specified term. A map of U.S. states will be generated in the window, compliant
    with state borders (outlines). The color of the state indicates the overall sentiment
    of all tweets containing the term in that state, with red meaning "awful sentiment" and
    green meaning "excellent sentiment." The height of the state itself corresponds to the
    number of tweets collected, regardless of positive or negative sentiment. Therefore, a state
    with a very long extrusion (more height) had more tweets containing that term than a state
    with a very shallow extrusion. Also, an 'invisible' or missing state indicates there were
    no tweets to be analyzed from that state and/or the overall average tweet sentiment was zero.
"""

from visual import *
from trends import *
from geo import *
import random

def windowSetup():   
    """" Sets up the VPython window "scene"
         See http://www.vpython.org/webdoc/visual/display.html"""
    
    scene.autoscale = False
    scene.background = (0.8, 1.0, 1.0)
    scene.foreground = color.black
    scene.height = 1000             #height of graphic window in pixels
    scene.width = 1000              #width of graphic window in pixels
    scene.up = (1, 0, 0)            #project the window around a vertical line along the x-axis
    scene.forward = (0, 0, 1)       #set camera pointing in the +z direction
    scene.center = (35, -100, -40) #adjust center to focus on U.S. map of state extrusions
    scene.lights = [distant_light(direction = (1, 1, 1), color = color.gray(0.1)),
                    distant_light(direction=(-1, -1, -1), color = color.gray(0.7))]
    scene.title = 'Twitter Trends'

def createTask6Dictionary(term):
    """ createTask6Dictionary returns a dictionary of the form
        created by Task 6 of Phase 1.
        
        The 'key is the state postal code.  The 'value' is a list of two numbers -
        the first is average sentiment for the state and the second is the number
        of tweets for the state.
           Inputs: term (chosen by the user when main function is called)
    """
    #return a dictionary of number of tweets & average sentiment mapped to state code strings
    return average_sentiments(group_tweets_by_state(load_tweets(make_tweet, term)))

def sentiment2Color(sentiment):
    ''' Returns a VPython color tuple depending on sentiment.
           Input: sentiment a float from -1.0 to 1.0

        Doctest for unit testing:
    >>> sentiment2Color(0.75)
    (0.2, 1, 0)
    >>> sentiment2Color(-0.45)
    (1.0, 0.3, 0)
    
    '''
    #conditional statement to decide color scheme assigned to each state's sentiment
    if -1.0 <= sentiment < -0.75:
        return (0.8, 0, 0) #deep red
    elif -0.75 <= sentiment < -0.6:
        return (1.0, 0, 0) #bright red
    elif -0.6 <= sentiment < -0.5:
        return (1.0, 0.1, 0) #red-orange
    elif -0.5 <= sentiment < -0.4:
        return (1.0, 0.3, 0) #dark orange
    elif -0.4 <= sentiment < -0.3:
        return (1, 0.4, 0) #orange
    elif -0.3 <= sentiment < -0.2:
        return (1, 0.5, 0) #yellow-orange
    elif -0.2 <= sentiment < -0.1:
        return (1, 0.7, 0) #dark yellow
    elif -0.1 <= sentiment < 0:
        return (1, 1.0, 0) #pure yellow
    elif 0 <= sentiment < 0.1:
        return (0.9, 1, 0) #green-yellow
    elif 0.1 <= sentiment < 0.2:
        return (0.8, 1, 0) #very light green
    elif 0.2 <= sentiment < 0.3:
        return (0.7, 1, 0) #light green
    elif 0.3 <= sentiment < 0.4:
        return (0.6, 1, 0) #green
    elif 0.4 <= sentiment < 0.75:
        return (0.4, 1, 0) #bright green
    elif 0.75 <= sentiment <= 1.0:
        return (0.2, 1, 0) #very bright green
    
    return (0, 0.0, 0.0) #black for error
       
def displaySentiments(myDict):
    """ Displays on a VPython graphics window a visualization of sentiments for U.S.
        states. Loads state outlines from the states.json file and generates 3D extrusions
        representing these states, adjusting the color and path (in the z-direction) of
        each state accordingly.
        input: myDict - dictionary in form returned by average_sentiments() function.
    """
    #retrieve coordinates of all state outlines in a dictionary
    stateDict = load_states()
    
    #loop through states within input dictionary's keys
    for state in myDict.keys():
        #create a 2D shape by giving a list of points from states.json file used by load_states()
        usState = stateDict[state]
        stateShape = shapes.pointlist(pos = usState[0])
        #create path along which to extrude the shape, scaling height to raw number of tweets
        num = -0.004 * myDict[state][1]
        path = [(0,0,0), (0,0,num)]
        path2 = [(0,0,-4), (0,0,-4.5)]
        #create extrusion object to extrude shape along the path
        ex = extrusion(pos = path, shape = stateShape,
                       color = sentiment2Color(myDict[state][0]))
        #uncomment to add outlines to define borders between adjacent states
        '''exOutline = extrusion(pos = path2, shape = usState[0], color = color.gray(0.8)'''
    
def main():
    windowSetup()
    term = input("Hello! Enter your desired search query: ")
    displaySentiments(createTask6Dictionary(term))

#call to main
main()

#needed for doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()
