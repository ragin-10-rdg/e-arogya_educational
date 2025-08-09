# E-Arogya Health Content Backend

A Django REST API backend for managing health education content including articles, videos, and educational resources across multiple health categories.

## 🏥 Features

- **Health Categories Management**: Nutrition, Hygiene, Child Health, Mental Health, First Aid, Seasonal Diseases
- **Media Content Management**: Videos, articles, PDFs, audio, infographics
- **Content Rating System**: User ratings and reviews
- **Analytics Tracking**: View counts, likes, shares
- **Search & Filtering**: Advanced search with relevance scoring
- **Admin Interface**: Full Django admin for content management
- **REST API**: Complete API for React Native/mobile app integration
- **Pre-populated Content**: 50+ curated health education resources

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone or navigate to the backend directory**:
   ```bash
   cd C:\Users\HPO\CascadeProjects\E-Arogya-Backend
   ```

2. **Run the automated setup**:
   ```bash
   python setup.py
   ```

   This will:
   - Install all dependencies
   - Create database migrations
   - Set up the database
   - Populate with health content
   - Optionally create a superuser

3. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

4. **Access the application**:
   - API: http://127.0.0.1:8000/api/
   - Admin: http://127.0.0.1:8000/admin/

## 📚 API Endpoints

### Health Categories
- `GET /api/categories/` - List all categories
- `GET /api/categories/{slug}/` - Get category details with content
- `GET /api/categories/{slug}/content/` - Get content for specific category
- `GET /api/categories/featured/` - Get categories with featured content

### Media Content
- `GET /api/content/` - List all content (with filtering)
- `GET /api/content/{id}/` - Get content details
- `POST /api/content/` - Create new content
- `PUT /api/content/{id}/` - Update content
- `DELETE /api/content/{id}/` - Delete content
- `GET /api/content/featured/` - Get featured content
- `GET /api/content/popular/` - Get popular content
- `GET /api/content/recent/` - Get recent content
- `GET /api/content/search/?q={query}` - Search content
- `POST /api/content/{id}/increment_view/` - Track content view
- `POST /api/content/{id}/like/` - Like content
- `POST /api/content/{id}/share/` - Track content share

### Content Ratings
- `GET /api/ratings/` - List ratings
- `POST /api/ratings/` - Create rating
- `GET /api/ratings/?content_id={id}` - Get ratings for specific content

### Statistics
- `GET /api/content/stats/` - Get content statistics

## 🎯 Pre-populated Content

The backend comes with 50+ curated health education resources:

### 🍎 Nutrition (6 items)
- WHO Healthy Diet Guidelines
- Academy of Nutrition resources
- MyPlate educational videos
- Food group songs and activities

### 🧼 Hygiene (4 items)
- Personal hygiene teaching activities
- Handwashing demonstration videos
- Dental care education
- SciShow Kids hygiene series

### 👶 Child Health (3 items)
- CDC vaccination schedules
- KidsHealth vaccine information
- Child development resources

### 🧠 Mental Health (6 items)
- Guided meditation videos
- Anxiety management channels
- Professional psychology resources
- Stress management techniques

### 🚑 First Aid (5 items)
- American Heart Association CPR training
- Hands-only CPR videos
- Emergency response guides
- Choking assistance tutorials

### 🌧️ Seasonal Diseases (3 items)
- Monsoon disease prevention
- Malaria and dengue prevention
- Expert medical advice videos

## 🔧 Adding New Content

### Via Django Admin
1. Go to http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Navigate to "Health Content" → "Media Content"
4. Click "Add Media Content"
5. Fill in the form and save

### Via API
```bash
POST /api/content/
Content-Type: application/json

{
  "category": 1,
  "title": "New Health Video",
  "description": "Educational content description",
  "content_type": "video",
  "url": "https://youtube.com/watch?v=example",
  "author": "Health Expert",
  "tags": "health, education, video",
  "is_featured": false
}
```

## 🎨 Frontend Integration

### React Native Example
```typescript
// services/healthApi.ts
const API_BASE_URL = 'http://127.0.0.1:8000/api';

export const healthApi = {
  getCategories: async () => {
    const response = await fetch(`${API_BASE_URL}/categories/`);
    return response.json();
  },
  
  getCategoryContent: async (slug: string) => {
    const response = await fetch(`${API_BASE_URL}/categories/${slug}/content/`);
    return response.json();
  },
  
  getFeaturedContent: async () => {
    const response = await fetch(`${API_BASE_URL}/content/featured/`);
    return response.json();
  }
};
```

## 🔒 Security Notes

- Change `SECRET_KEY` in production
- Set `DEBUG = False` in production
- Configure proper `ALLOWED_HOSTS`
- Use environment variables for sensitive settings
- Set up proper CORS settings for production

## 📊 Database Schema

### HealthCategory
- name, slug, description
- icon, color, order
- is_active, created_at, updated_at

### MediaContent
- title, slug, description, content_type
- url, thumbnail_url, embed_code
- author, source, duration, language
- difficulty_level, target_age_group
- is_featured, is_active, is_verified
- view_count, like_count, share_count
- tags, meta_description
- published_date, created_at, updated_at

### ContentRating
- content, user_ip, rating, comment
- created_at

### ContentView
- content, user_ip, user_agent
- viewed_at

## 🛠️ Development

### Manual Setup (Alternative)
```bash
# Install dependencies
pip install -r requirements.txt

# Create migrations
python manage.py makemigrations

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Populate content
python manage.py shell < populate_health_content.py

# Start server
python manage.py runserver
```

### Adding New Categories
1. Create category in admin or via API
2. Add content items for the category
3. Update frontend to display new category

### Customizing Content Types
Edit `CONTENT_TYPES` in `models.py` to add new content types like:
- `('podcast', 'Podcast')`
- `('webinar', 'Webinar')`
- `('quiz', 'Interactive Quiz')`

## 📱 Mobile App Integration

This backend is designed to work with the E-Arogya React Native app. The API provides:

- Category-based content organization
- Featured content for homepage
- Search functionality
- Content analytics
- User engagement tracking

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your content or features
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is created for educational purposes as part of the E-Arogya health education platform.

---

**E-Arogya Backend** - Empowering health education through technology 🏥💚
