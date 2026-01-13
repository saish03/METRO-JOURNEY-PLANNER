🚇 Metro Journey Planner

A Python-based Metro Journey Planner that helps users find the shortest and most efficient route between metro stations across Mumbai Metro and Pune Metro networks using graph algorithms.

📌 Features

Supports multiple cities (Mumbai & Pune). Uses Dijkstra’s Algorithm for shortest path calculation. City-wise metro network selection. Source and destination station input. Calculates minimum distance or cost. Simple command-line interface. Modular and easy-to-extend codebase.

🛠️ Technologies Used

Python 3, Graph Data Structures, Dijkstra’s Algorithm, VS Code, Git, GitHub.

⚙️ How It Works

The user selects a city. Metro stations are loaded as a graph. The user enters the source and destination stations. Dijkstra’s Algorithm computes the shortest path and minimum distance. The route is displayed in a readable format.

🧪 Sample Input / Output

Select City:

Mumbai

Pune

Enter source station: Andheri
Enter destination station: Ghatkopar

Shortest Path:
Andheri -> Jogeshwari -> Ghatkopar

Total Distance: 8 km

🧠 Algorithm Used

Dijkstra’s Algorithm is used to compute the shortest path in a weighted graph. It guarantees the optimal route between two stations. Time complexity is O(V²) and can be optimized using a priority queue.

🔮 Future Enhancements

Web-based user interface using Flask or Streamlit. Metro route map visualization. Travel time estimation. Fare calculation. Interchange optimization. Mobile-friendly interface.
