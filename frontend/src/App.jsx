function App() {
  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#F8F9FA",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <div
        style={{
          textAlign: "center",
          padding: "40px",
          maxWidth: "850px",
        }}
      >
        {/* Title */}
        <h1
          style={{
            color: "#4285F4",
            fontSize: "4rem",
            fontWeight: "700",
            marginBottom: "18px",
          }}
        >
          🎓 StudentMate AI
        </h1>

        {/* Subtitle */}
        <h2
          style={{
            color: "#34A853",
            fontSize: "2rem",
            fontWeight: "500",
            marginTop: "0",
            marginBottom: "35px",
            lineHeight: "1.4",
          }}
        >
          Multi-Agent AI Companion for Student Success
        </h2>

        {/* Description */}
        <p
          style={{
            color: "#555",
            fontSize: "22px",
            lineHeight: "1.8",
            maxWidth: "700px",
            margin: "0 auto",
          }}
        >
          Welcome to StudentMate AI.
          <br />
          Your intelligent AI companion that helps students learn,
          prepare for placements, plan studies, discover resources,
          and achieve academic success.
        </p>

        {/* Button */}
        <button
          style={{
            marginTop: "45px",
            padding: "16px 42px",
            border: "none",
            borderRadius: "10px",
            background: "#4285F4",
            color: "white",
            fontSize: "20px",
            fontWeight: "600",
            cursor: "pointer",
            transition: "0.3s",
          }}
        >
          Get Started
        </button>
      </div>
    </div>
  );
}

export default App;



