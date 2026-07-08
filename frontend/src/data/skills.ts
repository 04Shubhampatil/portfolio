export interface SkillCategory {
  title: string;
  description: string;
  icon: string;
  skills: string[];
  color: string;
}

export const skillsData: SkillCategory[] = [
  {
    title: "Frontend Development",
    description: "Building responsive and interactive user interfaces with modern JavaScript frameworks.",
    icon: "Layout",
    skills: [
      "HTML5",
      "CSS3",
      "JavaScript (ES6+)",
      "React.js",
      "Redux",
      "TypeScript",
      "Tailwind CSS",
      "Material UI"
    ],
    color: "bg-blue-50 border-blue-100 text-blue-700"
  },
  {
    title: "Backend Development",
    description: "Developing scalable server-side applications and secure RESTful APIs.",
    icon: "Server",
    skills: [
      "Node.js",
      "Express.js",
      "Firebase",
      "Supabase",
      "RESTful APIs",
      "JWT Authentication",
    
    ],
    color: "bg-emerald-50 border-emerald-100 text-emerald-700"
  },
  {
    title: "Databases",
    description: "Working with SQL and NoSQL databases for efficient data management.",
    icon: "Database",
    skills: [
      "MongoDB",
      "Mongoose",
      "MySQL"
    ],
    color: "bg-amber-50 border-amber-100 text-amber-700"
  },
  {
    title: "Tools & Deployment",
    description: "Version control, API testing, and deployment platforms used in modern development.",
    icon: "Cloud",
    skills: [
      "Git",
      "GitHub",
      "VS Code",
      "Postman",
      "Vercel",
      "Netlify"
    ],
    color: "bg-sky-50 border-sky-100 text-sky-700"
  },
  {
    title: "AI & Developer Tools",
    description: "Integrating AI services and developer tools into real-world applications.",
    icon: "Brain",
    skills: [
      "Google Gemini API",
      "Tesseract.js (OCR)",
      "GitHub Copilot",
      "Claude AI"
    ],
    color: "bg-indigo-50 border-indigo-100 text-indigo-700"
  }
];