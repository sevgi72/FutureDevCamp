function changeColor() {
    const colors = ['#FF5733', '#33FF57', '#3357FF', '#F1C40F', '#8E44AD'];
    let random = Math.random() * colors.length;
    const nameElement = document.getElementById('name');
    if (nameElement) {
        nameElement.style.color = colors[Math.floor(random)];
    }
}

document.addEventListener("DOMContentLoaded", function () {
    
    
    const toggleBtn = document.getElementById("toggle-about-btn");
    const aboutSection = document.getElementById("about-section");

    if (toggleBtn && aboutSection) {
        toggleBtn.addEventListener("click", function () {
            if (aboutSection.style.display === "none") {
                aboutSection.style.display = "block";
                toggleBtn.textContent = 'Hide About Me Section';
            } else {
                aboutSection.style.display = "none";
                toggleBtn.textContent = 'Show About Me Section';
            }
        });
    }

    
    const skillBtn = document.getElementById("add-skill-btn");
    const skillsList = document.getElementById("skills-list");

    if (skillBtn && skillsList) {
        skillBtn.addEventListener("click", function () {
            const category = prompt("Bacarıq kateqoriyasını daxil edin (örnək: Cloud Technologies):");
            if (!category) return; 
            
            const skills = prompt("Texnologiyaları daxil edin (örnək: AWS, Azure):");
            if (!skills) return;

            const newLi = document.createElement("li");
            newLi.innerHTML = `<strong>${category}:</strong> ${skills}`;
            skillsList.appendChild(newLi);
        });
    }

    
    const projectBtn = document.getElementById("add-project-btn");
    const projectsList = document.getElementById("projects-list");

    if (projectBtn && projectsList) {
        projectBtn.addEventListener("click", function () {
            const projName = prompt("Layihənin adini yazin:");
            if (!projName) return;

            const projType = prompt("Layihənin növünü yazin (MVC, API, Front-end və s.):");
            if (!projType) return;

            const projDesc = prompt("Layihə haqqinda qisa təsvir yazin:");
            if (!projDesc) return;

            const badgeClass = projType.toLowerCase().includes("mvc") ? "mvc" : 
                               projType.toLowerCase().includes("api") ? "api" : "front";

            const newLi = document.createElement("li");
            newLi.innerHTML = `
                <strong>${projName}</strong> 
                <span class="badge ${badgeClass}">${projType}</span>
                <a href="#" target="_blank" class="project-link">View Project →</a>
                <p class="project-desc">${projDesc}</p>
            `;            
            projectsList.appendChild(newLi);
        });
    }

    
    const welcomeBtn = document.getElementById("welcome-btn");
    
    if (welcomeBtn) {
        welcomeBtn.addEventListener("click", function () {
            const currentHour = new Date().getHours();
            let greetingMessage = "";

            if (currentHour >= 5 && currentHour < 12) {
                greetingMessage = "Sabahiniz xeyir";
            } else if (currentHour >= 12 && currentHour < 18) {
                greetingMessage = "Günortaniz xeyir";
            } else if (currentHour >= 18 && currentHour < 24) {
                greetingMessage = "Axşaminiz xeyir";
            } else {
                greetingMessage = "Gecəniz xeyirə qalsin";
            }

            alert(`${greetingMessage}\nPortfolio sehifeme xos gelmisiniz!`);
        });
    }
});