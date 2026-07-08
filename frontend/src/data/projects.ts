

export interface Project {
  id: string;
  category: string;
  title: string;
  thumbnail: string;
  fallbackThumbnail?: string;
  description: string;
  technologies: string[];
  links: { label: string; url: string }[];
  screenshots: string[];
  fallbackScreenshots?: string[];
}

export const projectsData: Project[] = [
  {
    id: "1",
    category: "AI Healthcare",
    title: "MediFlow - AI Hospital Management System",
    thumbnail: "/assets/projects/mediflow-thumb.png",
    fallbackThumbnail:
      "https://images.unsplash.com/photo-1576091160550-2173dba999ef?q=80&w=600&auto=format&fit=crop",
    description:
      "A full-stack AI-powered Hospital Management System with secure multi-role authentication for Patients, Doctors, and Admins. It analyzes uploaded medical reports using OCR and Google Gemini AI, automatically identifies medical specialties, and assigns patients to the most suitable doctor while tracking the complete treatment workflow.",
    technologies: [
      "React.js",
      "Node.js",
      "Express.js",
      "MongoDB",
      "Tailwind CSS",
      "JWT Authentication",
      "Google Gemini API",
      "Tesseract.js (OCR)"
    ],
    links: [

      {
        label: "Live Demo",
        url: "https://hospital-management-gamma-two.vercel.app"
      },
      {
        label: "GitHub Repository",
        url: "https://github.com/04Shubhampatil/hospital-management-.git"
      },

    ],
    screenshots: [
      "/assets/projects/mediflow-1.png",
      "/assets/projects/mediflow-2.png",
      "/assets/projects/mediflow-3.png"
    ],
    fallbackScreenshots: [
      "https://images.unsplash.com/photo-1516549655169-df83a0774514?q=80&w=1200&auto=format&fit=crop"
    ]
  },

  {
    id: "2",
    category: "AI Web Application",
    title: "Blogify - AI Food Recipe Blog",
    thumbnail: "/assets/projects/foodi-thumb.png",
    fallbackThumbnail:
      "https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=600&auto=format&fit=crop",
    description:
      "A MERN-based AI recipe application where users can explore, search, and generate personalized food recipes using the Google Gemini API. The application includes authentication, recipe management, responsive UI, and secure REST APIs.",
    technologies: [
      "React.js",
      "Node.js",
      "Express.js",
      "MongoDB",
      "Material UI",
      "Google Gemini API",
      "JWT Authentication"
    ],
    links: [

      {
        label: "Live Demo",
        url: "https://mern-foodi-app.onrender.com"
      },
      {
        label: "GitHub Repository",
        url: "https://github.com/04Shubhampatil/MERN-Foodi-App.git"
      }
    ],
    screenshots: [
      "/assets/projects/foodi-1.png",
      "/assets/projects/foodi-2.png"
    ],
    fallbackScreenshots: [
      "https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=1200&auto=format&fit=crop"
    ]
  },

  {
    id: "3",
    category: "Frontend Development",
    title: "Bike Accessories Landing Page",
    thumbnail: "/assets/projects/bike-thumb.png",
    fallbackThumbnail:
      "https://images.unsplash.com/photo-1558981806-ec527fa84c39?q=80&w=600&auto=format&fit=crop",
    description:
      "A modern and responsive React landing page for a bike accessories brand featuring clean UI, reusable components, smooth navigation, and a mobile-first design approach to showcase products effectively.",
    technologies: [
      "React.js",
      "JavaScript",
      "CSS3",
      "HTML5",
      "Tailwind CSS",
      "Responsive Design",
      "CSAP Animations"
    ],
    links: [
{
        label: "Live Demo",
        url: "https://bike-accesories.vercel.app/"
      },

      {
        label: "GitHub Repository",
        url: "https://github.com/04Shubhampatil/bike-accesories.git"
      }
    ],
    screenshots: [
      "/assets/projects/bike-1.png",
      "/assets/projects/bike-2.png"
    ],
    fallbackScreenshots: [
      "https://images.unsplash.com/photo-1502744688674-c619d1586c9e?q=80&w=1200&auto=format&fit=crop"
    ]
  },
  {
  id: "4",
  category: "Frontend Development",
  title: "AURA Smart Ring Landing Page",
  thumbnail: "/assets/projects/aura-thumb.png",
  fallbackThumbnail:
    "https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b?q=80&w=600&auto=format&fit=crop",

  description:
    "A modern and visually engaging product landing page for the AURA Smart Ring, built with React. The website features a futuristic dark theme, smooth scrolling, responsive layouts, animated product showcases, feature highlights, technical specifications, and an interactive user interface designed to deliver an immersive product presentation across all devices.",

  technologies: [
    "React.js",
    "JavaScript",
    "HTML5",
    "CSS3",
    "Tailwind CSS",
    "Responsive Design",
    "Framer Motion Animations"
  ],

  links: [
    {
      label: "Live Demo",
      url: "https://aura-smart-ring.vercel.app/"
    },
    {
      label: "GitHub Repository",
      url: "https://github.com/04Shubhampatil/aura-smart-ring.git"
    }
  ],

  screenshots: [
    "/assets/projects/aura-1.png",
    "/assets/projects/aura-2.png",
    "/assets/projects/aura-3.png"
  ],

  fallbackScreenshots: [
    "https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b?q=80&w=1200&auto=format&fit=crop"
  ]
}
];
