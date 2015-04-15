""" Using VPython label objects for displaying spheres with state postal codes
    Color of the spheres is based on Sentiment value in dictionary from Task 6
    of Phase 1.  The size of the sphere is related to the frequency of tweets in
    that state. """

""" WARNINGS about VPython's label ojects:
    Can't angle text with label object!
    Only a few fonts work! Some that work: times, monospace, sans, serif  """

from visual import *


def windowSetup():   
    """" Sets up the VPython window "scene"
         See http://www.vpython.org/webdoc/visual/display.html"""
    
    scene.autoscale = false        # Don't auto rescale
    scene.background = color.white
    scene.foreground = color.black
    scene.height = 1000            # height of graphic window in pixels
    scene.width = 1000             # width of graphic window in pixels
    scene.x = 100                  # x offset of upper left corner in pixels
    scene.y = 100                  # y offset of upper left corner in pixels
    scene.title = 'Twitter Trends'

def createTask6Dictionary():
    """ createTask6Dictionary returns a dictionary of the form
        created by Task 6 of Phase 1.
        
        The 'key is the state postal code.  The 'value' is a list of two numbers -
        the first is average sentiment for the state and the second is the number
        of tweets for the state.
           Inputs: none"""
    
    
    myDict = {'PA' : [1.0, 346], 'NY' : [-0.5, 234], 'NJ' : [-1.0, 45], \
              'VA' : [0.0, 101], 'MD' : [0.3, 401]}

    return myDict

def sentiment2Color(sentiment):
    ''' Returns a VPython color tuple depending on sentiment.
           Input: sentiment a float from -1.0 to 1.0

    Values for colors from http://en.wikipedia.org/wiki/List_of_colors:_A–F
    '''
    
    if -1.0 <= sentiment < -0.75:
        return (0.11, 0.11, 0.94) #Bluebonnet 
    elif -0.75 <= sentiment < -0.5:
        return (0.12, 0.46, 1.00) #Blue(Crayola)
    elif -0.5 <= sentiment < -0.25:
        return (0.12, 0.46, 1.00) #Capri
    elif -.25 <= sentiment < 0.0:
        return (0.67, 0.90, 0.93) #BlizzardBlue

    elif 0.0 <= sentiment < 0.25:
        return (1.0, 1.0, 1.0)    #White

    elif .25 <= sentiment < 0.5:
        return (0.94, 0.73, 0.80) #Cameo Pink
    elif .5 <= sentiment < 0.75:
        return (0.87, 0.44, 0.63) #China Pink
    elif .75 <= sentiment <= 1.0:
        return (1.0, 0.0, 0.22)   #Carmine Red
    
    return (0, 0.0, 0.0)          #Black for error
        

def testColors():
    ''' Test the colors of sentiment2Color() function with 8 spheres '''

    windowSetup()
    xpos = -8
    s = -1.0   
    for x in range(8):

       ball = sphere(pos=(xpos,0, 0), radius = 0.5, color = sentiment2Color(s))
       s += 0.25
       xpos += 1
       
def displaySentiments(myDict):
    """ Displays on a VPython graphics window a very simple visualization of
        average sentiments for the states.
        Very crude in calculating placement and size of the stateSpheres
        
            Input: myDict - dictionary in form returned by average_sentiments()
        function. """

    stateLabels = []
    stateSpheres = []

    # positions of the spheres in VPython coordinates
    # scene coordinates at top is 10, at left is -10, center is 0, 0
    xpos = -8
    ypos = 0
    lettersHeight = 10  # height for state code letters
    sphereScale = 1/200
    
    for state in myDict.keys():

      # radius based on number of tweets, color based on sentiment
      stateSpheres += [ sphere(pos=(xpos,0, 0), radius = myDict[state][1]*sphereScale, \
                             color = sentiment2Color(myDict[state][0]) ) ]
                        
      stateLabels += [ label(text = state, pos = (xpos, 0, 0),
                    color = (0.0, 0.0, 0.0),   # black
                    height = lettersHeight, box = 0, border = 0, font = "times") ]

      xpos += 4  # move over for the next sphere

    # How to access one of the labels in the list of label objects
    # and change an attribute's value
    # Uncomment the next line to change the first state code to green.
    stateLabels[0].color = (0.0, 1.0, 0.0)
    
def main():
    windowSetup()
    displaySentiments(createTask6Dictionary())
