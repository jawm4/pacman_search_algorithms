# Implemented algorithms and commands to use them.
# Full program is in pacman_app folder.
# Link to the course and source of the app: http://ai.berkeley.edu/project_overview.html


# Depth-First Search 
# Classic: python pacman.py -l bigMaze -p SearchAgent -a fn=dfs -z .5
# Open: python pacman.py -l openMaze -p SearchAgent -a fn=dfs -z .5
# Corner: python pacman.py -l bigCorners -p SearchAgent -a fn=dfs,prob=FoodSearchProblem -z .5
# Random: python pacman.py -l trickySearch -p SearchAgent -a fn=dfs,prob=FoodSearchProblem

def depthFirstSearch(problem):
	#loading the initial state
	beginning = problem.getStartState()
	
	#initialize the data structure, which sorts nodes to explore
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
					

# Breadth-First Search
# Classic: python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
# Open: python pacman.py -l openMaze -p SearchAgent -a fn=bfs -z .5
# Corner: python pacman.py -l bigCorners -p SearchAgent -a fn=bfs,prob=FoodSearchProblem -z .5
# Random: python pacman.py -l trickySearch -p SearchAgent -a fn=bfs,prob=FoodSearchProblem

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

# Uniform-Cost Search
# Classic: python pacman.py -l bigMaze -p SearchAgent -a fn=ucs -z .5
# Open: python pacman.py -l openMaze -p SearchAgent -a fn=ucs -z .5	
# Corner: python pacman.py -l bigCorners -p SearchAgent -a fn=ucs,prob=FoodSearchProblem -z .5	
# Random: python pacman.py -l trickySearch -p SearchAgent -a fn=ucs,prob=FoodSearchProblem			

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


# A-star
# Classic:
#	python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
#	python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
# Open:
#	python pacman.py -l openMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
#	python pacman.py -l openMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
# Corner:
#	python pacman.py -l bigCorners -p SearchAgent -a fn=astar,heuristic=foodHeuristic,prob=FoodSearchProblem -z .5
# Random:
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

def foodHeuristic(state, problem):
	#load current position of pacman and food matrix
	position, foodGrid = state
	#save matrix as list
	dots = foodGrid.asList()
	#empty list for BFS heuristics results
	distances = []
	
	#check if goal state
	if problem.isGoalState(state) == True:
		return 0
	
	for dot in dots:
		#function counting the distance between two points (position, dot)
		distance = mazeDistance(position, dot, problem.startingGameState)
		#sum it up
		distances = distances + [distance]
	# return maximum, which is the closest to exact heuristic	
	return max(distances)