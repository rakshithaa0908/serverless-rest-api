document.getElementById("regForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const msgDiv = document.getElementById("msg");
    msgDiv.textContent = "";

    const data = {
        first_name: document.getElementById("first_name").value,
        last_name: document.getElementById("last_name").value,
        address: document.getElementById("address").value,
        phno: document.getElementById("phno").value,
        email: document.getElementById("email").value,
    };

    try {
        const res = await fetch("https://ghanjduru2.execute-api.ap-south-1.amazonaws.com/proddeploy/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await res.json();

        if (res.status === 200) {
            msgDiv.textContent = "Registration successful";
            msgDiv.className = "message success";
            document.getElementById("regForm").reset();
        } else {
            msgDiv.textContent = "Failed: " + (result.message || "Unknown error");
            msgDiv.className = "message error";
        }
    } catch (err) {
        msgDiv.textContent = "Request failed";
        msgDiv.className = "message error";
    }
});
