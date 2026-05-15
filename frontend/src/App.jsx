import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [news, setNews] = useState([]);
  const [status, setStatus] = useState([]);
  const [search, setSearch] = useState("");

useEffect(() => {
  fetchNews();
  fetchStatus();

  const interval = setInterval(() => {
    fetchNews();
    fetchStatus();
  }, 300000); // 5 minuta

  return () => clearInterval(interval);
}, []);

  const fetchNews = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/processed-news"
      );

      setNews(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  const fetchStatus = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/status"
      );

      setStatus(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  const filteredNews = news.filter((item) =>
    item["Original Title"]
      ?.toLowerCase()
      .includes(search.toLowerCase())
  );

  return (
    <div className="container">
      <h1>Intelligent News Dashboard</h1>

      <div className="status-box">
        <h2>Status Notifications</h2>

        <ul>
          {status.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>

      <input
        type="text"
        placeholder="Search news..."
        className="search"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Original Title</th>
              <th>Rewritten Title</th>
              <th>Source</th>
            </tr>
          </thead>

          <tbody>
            {filteredNews.map((item, index) => (
              <tr key={index}>
                <td>{item.ID}</td>
                <td>{item["Original Title"]}</td>
                <td>{item["Rewritten Title"]}</td>
                <td>{item["Source Website"]}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;