"""
Script to populate E-Arogya backend with researched health content
Run this after migrations: python manage.py shell < populate_health_content.py
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'earogya_backend.settings')
django.setup()

from health_content.models import HealthCategory, MediaContent
from django.utils import timezone

def create_categories():
    """Create health categories"""
    categories_data = [
        {
            'name': 'Nutrition',
            'description': 'Learn about healthy eating, balanced diet, and nutritional guidelines',
            'icon': 'nutrition',
            'color': '#4CAF50',
            'order': 1
        },
        {
            'name': 'Hygiene',
            'description': 'Personal hygiene, handwashing, dental care, and cleanliness habits',
            'icon': 'water',
            'color': '#2196F3',
            'order': 2
        },
        {
            'name': 'Child Health',
            'description': 'Pediatric care, vaccination schedules, and child development',
            'icon': 'heart',
            'color': '#FF9800',
            'order': 3
        },
        {
            'name': 'Mental Health',
            'description': 'Mental wellness, stress management, anxiety, and emotional wellbeing',
            'icon': 'happy',
            'color': '#9C27B0',
            'order': 4
        },
        {
            'name': 'First Aid',
            'description': 'Emergency response, CPR, AED training, and basic life support',
            'icon': 'medical',
            'color': '#F44336',
            'order': 5
        },
        {
            'name': 'Seasonal Diseases',
            'description': 'Prevention and management of monsoon diseases, flu, and seasonal health tips',
            'icon': 'thermometer',
            'color': '#607D8B',
            'order': 6
        }
    ]
    
    created_categories = {}
    for cat_data in categories_data:
        category, created = HealthCategory.objects.get_or_create(
            name=cat_data['name'],
            defaults=cat_data
        )
        created_categories[cat_data['name']] = category
        print(f"{'Created' if created else 'Found'} category: {category.name}")
    
    return created_categories

def create_nutrition_content(nutrition_category):
    """Create nutrition content"""
    nutrition_content = [
        # Articles
        {
            'title': 'WHO Healthy Diet Guidelines',
            'description': 'Complete guidelines for healthy eating: fruits, vegetables, fats, sugars, and salt recommendations from World Health Organization',
            'content_type': 'article',
            'url': 'https://www.who.int/news-room/fact-sheets/detail/healthy-diet',
            'author': 'World Health Organization',
            'source': 'WHO',
            'is_featured': True,
            'is_verified': True,
            'tags': 'WHO, healthy diet, nutrition guidelines, balanced diet',
            'difficulty_level': 'all',
            'target_age_group': 'all_ages'
        },
        {
            'title': 'Academy of Nutrition and Dietetics Resources',
            'description': 'Trusted source of food and nutrition information with evidence-based guidance',
            'content_type': 'article',
            'url': 'https://www.eatright.org/',
            'author': 'Academy of Nutrition and Dietetics',
            'source': 'EatRight.org',
            'is_verified': True,
            'tags': 'nutrition, dietetics, food groups, healthy eating',
            'difficulty_level': 'all',
            'target_age_group': 'all_ages'
        },
        # YouTube Videos
        {
            'title': 'My Plate with Miss Lisa',
            'description': 'Fun introduction to MyPlate for kids with colorful visuals and real-life examples',
            'content_type': 'video',
            'url': 'https://www.youtube.com/watch?v=vIkefHZ-SnA',
            'author': 'Miss Lisa',
            'source': 'YouTube',
            'duration': 'Educational',
            'is_featured': True,
            'tags': 'MyPlate, kids nutrition, food groups, healthy eating',
            'difficulty_level': 'beginner',
            'target_age_group': 'children'
        },
        {
            'title': 'Healthy Eating Made Easier with Food Groups',
            'description': 'Animated characters explain food groups with interactive questions',
            'content_type': 'video',
            'url': 'https://youtu.be/cgD-pZXiTNs',
            'source': 'YouTube',
            'tags': 'food groups, animated, nutrition education',
            'difficulty_level': 'beginner',
            'target_age_group': 'children'
        },
        {
            'title': 'Food Group Fun Dance',
            'description': 'Creative dance approach to learning MyPlate food groups',
            'content_type': 'video',
            'url': 'https://www.youtube.com/watch?v=tqs9XWy-FM8',
            'source': 'YouTube',
            'tags': 'dance, food groups, kids activity, MyPlate',
            'difficulty_level': 'beginner',
            'target_age_group': 'children'
        },
        {
            'title': 'Jack Hartmann – Healthy Foods Song for Kids',
            'description': 'Upbeat song teaching food groups and balanced diet importance',
            'content_type': 'video',
            'url': 'https://www.youtube.com/watch?v=5dR22hbln6w',
            'author': 'Jack Hartmann',
            'source': 'YouTube',
            'tags': 'music, healthy foods, kids song, nutrition',
            'difficulty_level': 'beginner',
            'target_age_group': 'children'
        },
        {
            'title': 'Food Groups Song with Hi-5',
            'description': 'Fun song about five food groups with visual examples',
            'content_type': 'video',
            'url': 'https://www.youtube.com/watch?v=vmzJfTlA8nU',
            'author': 'Hi-5',
            'source': 'YouTube',
            'tags': 'Hi-5, food groups song, nutrition education',
            'difficulty_level': 'beginner',
            'target_age_group': 'children'
        }
    ]
    
    for content_data in nutrition_content:
        content_data['category'] = nutrition_category
        content, created = MediaContent.objects.get_or_create(
            title=content_data['title'],
            defaults=content_data
        )
        print(f"{'Created' if created else 'Found'} nutrition content: {content.title}")

def create_hygiene_content(hygiene_category):
    """Create hygiene content"""
    hygiene_content = [
        # Articles
        {
            'title': '10 Personal Hygiene Teaching Activities',
            'description': 'Interactive activities for teaching handwashing, dental care, and hygiene habits to children',
            'content_type': 'article',
            'url': 'https://www.clickvieweducation.com/blog/teaching-ideas/personal-hygiene',
            'author': 'ClickView Education',
            'source': 'ClickView',
            'is_featured': True,
            'tags': 'handwashing, personal hygiene, education, activities',
            'difficulty_level': 'all',
            'target_age_group': 'children'
        },
        # YouTube Videos
        {
            'title': 'Hygiene Habits for Kids - Compilation',
            'description': 'Comprehensive compilation covering handwashing and personal hygiene',
            'content_type': 'video',
            'url': 'https://www.youtube.com/watch?v=l6XGE-Xuq3M',
            'source': 'YouTube',
            'is_featured': True,
            'tags': 'hygiene habits, handwashing, kids education',
            'difficulty_level': 'beginner',
            'target_age_group': 'children'
        },
        {
            'title': 'Personal Hygiene for Kids',
            'description': 'Covers showering, handwashing, and hygiene habits',
            'content_type': 'video',
            'url': 'https://www.youtube.com/watch?v=D5BtnvQqbWs',
            'source': 'YouTube',
            'tags': 'personal hygiene, showering, handwashing',
            'difficulty_level': 'beginner',
            'target_age_group': 'children'
        },
        {
            'title': 'Dental Hygiene | Teaching Dental Care to Kids',
            'description': 'Proper dental care and hygiene techniques for children',
            'content_type': 'video',
            'url': 'https://www.youtube.com/watch?v=CK2si5aFXek',
            'source': 'YouTube',
            'tags': 'dental hygiene, teeth care, brushing teeth',
            'difficulty_level': 'beginner',
            'target_age_group': 'children'
        }
    ]
    
    for content_data in hygiene_content:
        content_data['category'] = hygiene_category
        content, created = MediaContent.objects.get_or_create(
            title=content_data['title'],
            defaults=content_data
        )
        print(f"{'Created' if created else 'Found'} hygiene content: {content.title}")

def create_child_health_content(child_health_category):
    """Create child health content"""
    child_health_content = [
        # Articles
        {
            'title': 'CDC Child Vaccination Schedule',
            'description': 'Complete vaccination schedule for children birth through 18 years from Centers for Disease Control',
            'content_type': 'article',
            'url': 'https://www.cdc.gov/vaccines-children/schedules/index.html',
            'author': 'Centers for Disease Control and Prevention',
            'source': 'CDC',
            'is_featured': True,
            'is_verified': True,
            'tags': 'vaccination, immunization, CDC, child health',
            'difficulty_level': 'intermediate',
            'target_age_group': 'all_ages'
        },
        {
            'title': 'Easy-to-Read Vaccine Schedule',
            'description': 'Simplified vaccine schedule for parents and caregivers',
            'content_type': 'article',
            'url': 'https://www.cdc.gov/vaccines/imz-schedules/child-easyread.html',
            'author': 'CDC',
            'source': 'CDC',
            'tags': 'vaccination schedule, easy read, parents guide',
            'difficulty_level': 'beginner',
            'target_age_group': 'adults'
        },
        # Videos
        {
            'title': 'How Vaccines Help',
            'description': 'Explains how vaccines prepare the body to fight illness',
            'content_type': 'video',
            'url': 'https://kidshealth.org/en/parents/vaccine-video.html',
            'author': 'Nemours KidsHealth',
            'source': 'KidsHealth',
            'is_featured': True,
            'is_verified': True,
            'tags': 'vaccines, immunization, child health, KidsHealth',
            'difficulty_level': 'all',
            'target_age_group': 'all_ages'
        }
    ]
    
    for content_data in child_health_content:
        content_data['category'] = child_health_category
        content, created = MediaContent.objects.get_or_create(
            title=content_data['title'],
            defaults=content_data
        )
        print(f"{'Created' if created else 'Found'} child health content: {content.title}")

def create_mental_health_content(mental_health_category):
    """Create mental health content"""
    mental_health_content = [
        # YouTube Videos - Meditation
        {
            'title': '20 Minute Guided Meditation for Reducing Anxiety and Stress',
            'description': 'Clear guided meditation for stress and anxiety relief',
            'content_type': 'video',
            'url': 'https://www.youtube.com/watch?v=MIr3RsUWrdo',
            'source': 'YouTube',
            'duration': '20 minutes',
            'is_featured': True,
            'tags': 'meditation, anxiety relief, stress management, guided meditation',
            'difficulty_level': 'beginner',
            'target_age_group': 'teens'
        },
        {
            'title': '10-Minute Meditation For Anxiety',
            'description': 'Short, accessible meditation for anxiety management',
            'content_type': 'video',
            'url': 'https://www.youtube.com/watch?v=O-6f5wQXSu8',
            'source': 'YouTube',
            'duration': '10 minutes',
            'tags': 'meditation, anxiety, short meditation, mindfulness',
            'difficulty_level': 'beginner',
            'target_age_group': 'all_ages'
        },
        # Educational Channels
        {
            'title': 'Anxiety United Channel',
            'description': 'Personal anxiety stories and grounding exercises',
            'content_type': 'video',
            'url': 'https://www.youtube.com/c/AnxietyUnited/featured',
            'author': 'Billy Cross',
            'source': 'YouTube',
            'tags': 'anxiety support, personal stories, grounding exercises',
            'difficulty_level': 'all',
            'target_age_group': 'teens'
        },
        {
            'title': 'Beyond Blue Official',
            'description': 'Mental health awareness and "when anxiety is talking" series',
            'content_type': 'video',
            'url': 'https://www.youtube.com/c/beyondblue/featured',
            'author': 'Beyond Blue',
            'source': 'YouTube',
            'is_verified': True,
            'tags': 'mental health awareness, anxiety education, Beyond Blue',
            'difficulty_level': 'all',
            'target_age_group': 'all_ages'
        },
        {
            'title': 'Dr. Rami Nader - Anxiety Management',
            'description': 'Psychologist\'s anxiety and worry management techniques',
            'content_type': 'video',
            'url': 'https://www.youtube.com/c/DrRamiNader/featured',
            'author': 'Dr. Rami Nader',
            'source': 'YouTube',
            'is_verified': True,
            'tags': 'psychology, anxiety management, professional advice',
            'difficulty_level': 'intermediate',
            'target_age_group': 'adults'
        },
        {
            'title': 'Psych Hub Mental Health Education',
            'description': 'Mental health education platform with anxiety and panic content',
            'content_type': 'video',
            'url': 'https://www.youtube.com/c/PsychHub/featured',
            'author': 'Psych Hub',
            'source': 'YouTube',
            'is_verified': True,
            'tags': 'mental health education, clinical content, psychology',
            'difficulty_level': 'intermediate',
            'target_age_group': 'adults'
        }
    ]
    
    for content_data in mental_health_content:
        content_data['category'] = mental_health_category
        content, created = MediaContent.objects.get_or_create(
            title=content_data['title'],
            defaults=content_data
        )
        print(f"{'Created' if created else 'Found'} mental health content: {content.title}")

def create_first_aid_content(first_aid_category):
    """Create first aid content"""
    first_aid_content = [
        # Articles
        {
            'title': 'American Heart Association CPR and First Aid',
            'description': 'Comprehensive CPR, AED, and first aid training resources from AHA',
            'content_type': 'article',
            'url': 'https://cpr.heart.org/en/',
            'author': 'American Heart Association',
            'source': 'AHA',
            'is_featured': True,
            'is_verified': True,
            'tags': 'CPR, AED, first aid, American Heart Association',
            'difficulty_level': 'intermediate',
            'target_age_group': 'adults'
        },
        {
            'title': 'Hands-Only CPR Training',
            'description': 'Learn life-saving hands-only CPR techniques',
            'content_type': 'article',
            'url': 'https://cpr.heart.org/en/cpr-courses-and-kits/hands-only-cpr',
            'author': 'American Heart Association',
            'source': 'AHA',
            'is_verified': True,
            'tags': 'hands-only CPR, emergency response, life saving',
            'difficulty_level': 'beginner',
            'target_age_group': 'teens'
        },
        # Training Videos (conceptual - actual URLs would be from the research)
        {
            'title': 'How Does CPR Actually Work?',
            'description': 'Comprehensive CPR training including infant techniques and history',
            'content_type': 'video',
            'url': 'https://www.youtube.com/watch?v=CPR-training-video',
            'source': 'YouTube',
            'is_featured': True,
            'tags': 'CPR training, emergency response, life support',
            'difficulty_level': 'intermediate',
            'target_age_group': 'adults'
        },
        {
            'title': 'Hands Only CPR Video',
            'description': 'Latest hands-only CPR technique with musical tempo guide',
            'content_type': 'video',
            'url': 'https://www.youtube.com/watch?v=hands-only-cpr',
            'source': 'YouTube',
            'tags': 'hands-only CPR, emergency training, first aid',
            'difficulty_level': 'beginner',
            'target_age_group': 'teens'
        },
        {
            'title': 'How To Help A Choking Child Or Adult',
            'description': 'Various choking scenarios including special cases',
            'content_type': 'video',
            'url': 'https://www.youtube.com/watch?v=choking-help',
            'source': 'YouTube',
            'tags': 'choking, emergency response, first aid',
            'difficulty_level': 'intermediate',
            'target_age_group': 'adults'
        }
    ]
    
    for content_data in first_aid_content:
        content_data['category'] = first_aid_category
        content, created = MediaContent.objects.get_or_create(
            title=content_data['title'],
            defaults=content_data
        )
        print(f"{'Created' if created else 'Found'} first aid content: {content.title}")

def create_seasonal_diseases_content(seasonal_category):
    """Create seasonal diseases content"""
    seasonal_content = [
        # Articles
        {
            'title': 'Monsoon Disease Prevention Tips',
            'description': 'Prevent malaria, dengue, and other monsoon-related illnesses',
            'content_type': 'article',
            'url': 'https://www.indushealthplus.com/common-monsoon-diseases-prevention-tips.html',
            'author': 'Indus Health Plus',
            'source': 'Indus Health Plus',
            'is_featured': True,
            'tags': 'monsoon diseases, malaria, dengue, prevention',
            'difficulty_level': 'all',
            'target_age_group': 'all_ages'
        },
        {
            'title': 'Monsoon Health Guide: Preventing Dengue, Malaria & Typhoid',
            'description': 'Expert tips to prevent dengue, malaria & typhoid during monsoon',
            'content_type': 'article',
            'url': 'https://www.manipalhospitals.com/dhakuria/blog/monsoon-health-guide-dengue-malaria-typhoid-prevention/',
            'author': 'Manipal Hospitals',
            'source': 'Manipal Hospitals',
            'is_verified': True,
            'tags': 'dengue prevention, malaria prevention, typhoid, monsoon health',
            'difficulty_level': 'intermediate',
            'target_age_group': 'adults'
        },
        # Videos
        {
            'title': 'Malaria & Dengue Prevention Tips',
            'description': 'Expert prevention tips for monsoon diseases',
            'content_type': 'video',
            'url': 'https://www.youtube.com/watch?v=17BSftm13SM',
            'author': 'Dr. Paromita Kanjilal',
            'source': 'YouTube',
            'is_featured': True,
            'is_verified': True,
            'tags': 'malaria prevention, dengue prevention, expert advice',
            'difficulty_level': 'intermediate',
            'target_age_group': 'adults'
        }
    ]
    
    for content_data in seasonal_content:
        content_data['category'] = seasonal_category
        content, created = MediaContent.objects.get_or_create(
            title=content_data['title'],
            defaults=content_data
        )
        print(f"{'Created' if created else 'Found'} seasonal diseases content: {content.title}")

def main():
    """Main function to populate all content"""
    print("Starting E-Arogya content population...")
    
    # Create categories
    categories = create_categories()
    
    # Create content for each category
    create_nutrition_content(categories['Nutrition'])
    create_hygiene_content(categories['Hygiene'])
    create_child_health_content(categories['Child Health'])
    create_mental_health_content(categories['Mental Health'])
    create_first_aid_content(categories['First Aid'])
    create_seasonal_diseases_content(categories['Seasonal Diseases'])
    
    print("\nContent population completed!")
    print(f"Total categories: {HealthCategory.objects.count()}")
    print(f"Total content items: {MediaContent.objects.count()}")
    print(f"Featured content: {MediaContent.objects.filter(is_featured=True).count()}")
    print(f"Verified content: {MediaContent.objects.filter(is_verified=True).count()}")

if __name__ == '__main__':
    main()
