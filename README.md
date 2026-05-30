# intelligent-campus-navigation-assistant
Intelligent Campus Navigation Assistant is an AI-based navigation system that finds optimal routes between campus locations using graph search algorithms such as BFS, UCS, and A*. The project demonstrates intelligent agent design, pathfinding, and route optimization through an interactive campus map interface.

Features
Interactive campus map visualization
Source and destination selection
AI search algorithms:
BFS
UCS
A*
Route distance calculation
Agent execution logs
PEAS model representation
Real-time path highlighting
PEAS Model
Component	Description
Performance	Find the shortest and correct route
Environment	Static campus graph
Actuators	Route visualization and directions
Sensors	User inputs and campus map data
Campus Locations
Library
Hostel
Admin Block
C Block
Canteen
Sports Ground
Lab Complex
Algorithms Used
Breadth-First Search (BFS)

Finds paths by exploring nodes level by level.

Uniform Cost Search (UCS)

Finds the least-cost route using edge weights.

A* Search

Uses path cost and a heuristic estimate for faster route finding.

f(n)=g(n)+h(n)

Where:

g(n) = actual path cost
h(n) = estimated distance to goal
Workflow
Select source and destination.
Choose BFS, UCS, or A*.
Click Find Route.
View:
Optimal path
Total distance
Explored nodes
Agent logs
Technologies Used
HTML5
CSS3
JavaScript
SVG Graphics
Artificial Intelligence Search Algorithms
Future Enhancements
Real-time navigation
GPS integration
Dynamic obstacle handling
Mobile support
Additional search algorithms
Conclusion

This project demonstrates how intelligent agents use search algorithms to solve navigation problems efficiently. It provides a practical implementation of AI concepts such as graph search, heuristic reasoning, and the PEAS framework in a campus navigation scenario.
