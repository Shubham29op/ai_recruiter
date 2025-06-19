import React, { useState } from "react";
import axios from "axios";

const ResumeUpload = () => {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

const handleUpload = async () => {
  const formData = new FormData();
  formData.append("file", file);            // ✅ required
  formData.append("user_id", "12345");      // ✅ also required by FastAPI

  try {
    const response = await axios.post("http://127.0.0.1:8000/api/resume/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data"
      }
    });
    console.log("Upload success:", response.data);
    setResponse(response.data);
  } catch (error) {
    console.error("Upload error:", error);
  }
};


  return (
    <div className="p-6 border rounded shadow max-w-xl mx-auto mt-10 bg-white">
      <h2 className="text-2xl font-semibold mb-4">Upload Resume</h2>
      <input type="file" accept=".pdf,.doc,.docx" onChange={handleFileChange} />
      <button
        onClick={handleUpload}
        className="mt-3 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        disabled={loading}
      >
        {loading ? "Uploading..." : "Upload"}
      </button>

      {response && (
        <div className="mt-6 bg-gray-100 p-4 rounded">
          <h3 className="font-semibold">Parsed Output:</h3>
          <pre className="text-sm mt-2">{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default ResumeUpload;
