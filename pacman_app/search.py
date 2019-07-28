# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from game import Directions
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

#DFS 
#KLASYCZNY:
#	python pacman.py -l bigMaze -p SearchAgent -a fn=dfs -z .5
#OTWARTY:
#	python pacman.py -l openMaze -p SearchAgent -a fn=dfs -z .5
#KRANCE
#	python pacman.py -l bigCorners -p SearchAgent -a fn=dfs,prob=FoodSearchProblem -z .5
#LOSOWY
#	python pacman.py -l trickySearch -p SearchAgent -a fn=dfs,prob=FoodSearchProblem
def depthFirstSearch(problem):
	#loading the initial state
	beginning = problem.getStartState()
	
	#initialize the queue, which shows which nodes we have to explore
	#it comes from util.py
	fringe = util.Stack()
	#create empty list for final path
	path = []
	#create empty set to store visited nodes
	checked = set()
	#put it all into the fringe
	fringe.push((beginning, path, checked))
	
	#loop until any stop condition
	while 1:
		if (fringe.isEmpty()):
			return 0
		
		#take data from the fringe
		node, path, checked = fringe.pop()
		
		#check if it is a goal state
		if problem.isGoalState(node) == True:
			return path		
		
		if node not in checked:
			checked.add(node)
			#load nodes successors
			successors = problem.getSuccessors(node)
			for successor, direction, steps in successors:
				if successor not in checked:
					#add successors to the fringe
					fringe.push((successor, path + [direction], checked))
					

#BFS
#KLASAYCZNY:
#	python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
#OTWARTY:
#	python pacman.py -l openMaze -p SearchAgent -a fn=bfs -z .5
#KRANCE:
#	python pacman.py -l bigCorners -p SearchAgent -a fn=bfs,prob=FoodSearchProblem -z .5
#LOSOWY
#	python pacman.py -l trickySearch -p SearchAgent -a fn=bfs,prob=FoodSearchProblem
def breadthFirstSearch(problem):
	beginning = problem.getStartState()
	#the only difference - data structure
	fringe = util.Queue()
	path = []
	checked = set()
	fringe.push((beginning, path, checked))
	
	while 1:
		if (fringe.isEmpty()):
			return 0
		
		node, path, checked = fringe.pop()
		
		if problem.isGoalState(node) == True:
			return path		
		
		if node not in checked:
			checked.add(node)
			successors = problem.getSuccessors(node)
			for successor, direction, steps in successors:
				if successor not in checked:
					fringe.push((successor, path + [direction], checked))

#UCS
#KLASYCZNY:
#	python pacman.py -l bigMaze -p SearchAgent -a fn=ucs -z .5
#OTWARTY:
#	python pacman.py -l openMaze -p SearchAgent -a fn=ucs -z .5	
#KRANCE:
#	python pacman.py -l bigCorners -p SearchAgent -a fn=ucs,prob=FoodSearchProblem -z .5	
#LOSOWY
#	python pacman.py -l trickySearch -p SearchAgent -a fn=ucs,prob=FoodSearchProblem			
def uniformCostSearch(problem):
	beginning = problem.getStartState()
	fringe = util.PriorityQueue()
	path = []
	checked = set()
	#initialize depth counter as an additional argument (cost)
	depth = 0
	fringe.push((beginning, path, checked, depth), 0)
	
	while 1:
		if (fringe.isEmpty() == True):
			return 0
		
		node, path, checked, depth = fringe.pop()
		
		if problem.isGoalState(node) == True:
			return path		
		
		if node not in checked:
			checked.add(node)
			successors = problem.getSuccessors(node)
			for successor, direction, steps in successors:
				if successor not in checked:
					fringe.push((successor, path + [direction], checked, depth + steps), depth + steps)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
#A*
#KLASYCZNY:
#	python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
#	python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
#OTWARTY:
#	python pacman.py -l openMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
#	python pacman.py -l openMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
#KRANCE:
#	python pacman.py -l bigCorners -p SearchAgent -a fn=astar,heuristic=foodHeuristic,prob=FoodSearchProblem -z .5
#LOSOWY
#	python pacman.py -l trickySearch -p SearchAgent -a fn=astar,prob=FoodSearchProblem,heuristic=foodHeuristic
def aStarSearch(problem, heuristic=nullHeuristic):
	beginning = problem.getStartState()
	fringe = util.PriorityQueue()
	path = []
	checked = set()
	depth = 0
	fringe.push((beginning, path, checked, depth), 0)
	
	while 1:
		if (fringe.isEmpty() == True):
			return 0
		
		node, path, checked, depth = fringe.pop()
		
		if problem.isGoalState(node) == True:
			return path		
		
		if node not in checked:
			checked.add(node)
			successors = problem.getSuccessors(node)
			for successor, direction, steps in successors:
				if successor not in checked:
					#taking heuristic into consideration when counting steps/depth to goal
					total_steps = depth + steps
					fringe.push((successor, path+[direction], checked, total_steps), total_steps+heuristic(successor, problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
