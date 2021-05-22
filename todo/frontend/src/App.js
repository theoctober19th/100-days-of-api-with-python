import logo from './logo.svg';
import './App.css';
import { Component } from 'react'
import axios from 'axios'

class App extends Component {
  state = {
    todos: []
  }

  componentDidMount() {
    this.getTodos();
  }

  getTodos() {
    axios.get("http://localhost:8000/api/")
      .then(res => {
        this.setState(
          {
            todos: res.data
          }
        );
      }).catch(err => console.log(err));
  }

  render() {
    return (
      <div>
        {this.state.todos.map(todo => (
          <div key={todo.id}>
            <h1>{todo.title}</h1>
            <p>{todo.description}</p>
          </div>
        ))}
      </div>
    )
  }
}

export default App;
