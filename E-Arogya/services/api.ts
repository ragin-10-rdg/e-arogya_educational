// Mock API service for E-Arogya app
export interface Article {
  id: string;
  title: string;
  description: string;
  content: string;
  category: string;
  imageUrl?: string;
  publishedDate: string;
}

export interface Video {
  id: string;
  title: string;
  description: string;
  thumbnailUrl?: string;
  videoUrl: string;
  duration: string;
  category: string;
  publishedDate: string;
}

// Mock data for articles
const mockArticles: Article[] = [
  {
    id: '1',
    title: 'Balanced Diet Essentials',
    description: 'Learn about the importance of a balanced diet for optimal health.',
    content: 'A balanced diet includes all essential nutrients...',
    category: 'nutrition',
    imageUrl: 'https://via.placeholder.com/300x200',
    publishedDate: '2024-01-15'
  },
  {
    id: '2',
    title: 'Proper Hand Washing Techniques',
    description: 'Step-by-step guide to effective hand hygiene.',
    content: 'Proper hand washing is crucial for preventing infections...',
    category: 'hygiene',
    imageUrl: 'https://via.placeholder.com/300x200',
    publishedDate: '2024-01-10'
  },
  {
    id: '3',
    title: 'Child Vaccination Schedule',
    description: 'Complete guide to childhood immunizations.',
    content: 'Vaccinations protect children from serious diseases...',
    category: 'child-health',
    imageUrl: 'https://via.placeholder.com/300x200',
    publishedDate: '2024-01-20'
  },
  {
    id: '4',
    title: 'Managing Stress and Anxiety',
    description: 'Effective strategies for mental wellness.',
    content: 'Mental health is as important as physical health...',
    category: 'mental-health',
    imageUrl: 'https://via.placeholder.com/300x200',
    publishedDate: '2024-01-18'
  },
  {
    id: '5',
    title: 'Basic First Aid Techniques',
    description: 'Essential first aid skills everyone should know.',
    content: 'First aid can save lives in emergency situations...',
    category: 'first-aid',
    imageUrl: 'https://via.placeholder.com/300x200',
    publishedDate: '2024-01-12'
  },
  {
    id: '6',
    title: 'Seasonal Flu Prevention',
    description: 'How to protect yourself during flu season.',
    content: 'Seasonal diseases require specific preventive measures...',
    category: 'seasonal-diseases',
    imageUrl: 'https://via.placeholder.com/300x200',
    publishedDate: '2024-01-25'
  }
];

// Mock data for videos
const mockVideos: Video[] = [
  {
    id: '1',
    title: 'Healthy Cooking Basics',
    description: 'Learn to prepare nutritious meals at home.',
    thumbnailUrl: 'https://via.placeholder.com/300x200',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    duration: '10:30',
    category: 'nutrition',
    publishedDate: '2024-01-16'
  },
  {
    id: '2',
    title: 'Personal Hygiene Routine',
    description: 'Daily hygiene practices for better health.',
    thumbnailUrl: 'https://via.placeholder.com/300x200',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    duration: '8:45',
    category: 'hygiene',
    publishedDate: '2024-01-11'
  },
  {
    id: '3',
    title: 'Child Safety at Home',
    description: 'Creating a safe environment for children.',
    thumbnailUrl: 'https://via.placeholder.com/300x200',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    duration: '12:15',
    category: 'child-health',
    publishedDate: '2024-01-21'
  },
  {
    id: '4',
    title: 'Meditation for Beginners',
    description: 'Simple meditation techniques for stress relief.',
    thumbnailUrl: 'https://via.placeholder.com/300x200',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    duration: '15:00',
    category: 'mental-health',
    publishedDate: '2024-01-19'
  },
  {
    id: '5',
    title: 'CPR Training Video',
    description: 'Learn life-saving CPR techniques.',
    thumbnailUrl: 'https://via.placeholder.com/300x200',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    duration: '20:30',
    category: 'first-aid',
    publishedDate: '2024-01-13'
  },
  {
    id: '6',
    title: 'Winter Health Tips',
    description: 'Staying healthy during cold season.',
    thumbnailUrl: 'https://via.placeholder.com/300x200',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    duration: '9:20',
    category: 'seasonal-diseases',
    publishedDate: '2024-01-26'
  }
];

// Simulate API delay
const delay = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

// Mock API functions
export const fetchArticlesByCategory = async (category: string): Promise<Article[]> => {
  await delay(1000); // Simulate network delay
  return mockArticles.filter(article => article.category === category);
};

export const fetchVideosByCategory = async (category: string): Promise<Video[]> => {
  await delay(1000); // Simulate network delay
  return mockVideos.filter(video => video.category === category);
};

export const fetchAllArticles = async (): Promise<Article[]> => {
  await delay(1000);
  return mockArticles;
};

export const fetchAllVideos = async (): Promise<Video[]> => {
  await delay(1000);
  return mockVideos;
};
