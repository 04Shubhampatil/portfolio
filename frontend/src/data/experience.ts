export interface Experience {
  id: string;
  period: string;
  company: string;
  role: string;
  startMonth: string;
  endMonth: string;
  ongoing: boolean;
  bullets: string[];
  logo?: string;
}

export const experienceData: Experience[] = [
  {
    id: "1",
    period: "2025-Present",
    company: "Felix-IT Systems",
    role: "Full-Stack Developer Intern",
    startMonth: "Jan 2025",
    endMonth: "Present",
    ongoing: true,
    logo: "/assets/projects/felix_logo.png",
    bullets: [
      "Developed and optimized end-to-end full-stack web applications using React.js, Node.js, Express.js, and MongoDB.",
      "Built reusable and responsive UI components while collaborating in Agile sprints, improving cross-browser and mobile compatibility.",
      "Designed and integrated secure RESTful APIs to enable efficient communication between frontend and backend systems.",
      "Performed application testing, debugging, and peer code reviews to ensure clean, maintainable, and high-quality code.",
    ],
  },
];
