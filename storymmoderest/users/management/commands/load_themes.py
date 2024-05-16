from django.core.management.base import BaseCommand
from storymmoderest.users.models import Theme

class Command(BaseCommand):
    help = 'This handles loading of themes into a new database.'

    def handle(self, *args, **options):
        Theme.objects.all().delete()

        Theme.objects.create(
            name="Refined Light",
            description="A refined light mode theme emphasizing a harmonious color palette. Soft blues and grays provide a serene and professional backdrop, with subtle accents for a cohesive look.",
            primary_color="#607D8B",  # Blue Grey for primary interface elements
            secondary_color="#CFD8DC",  # Light Blue Grey for secondary items
            accent_color="#80CBC4",  # Teal for accent pieces, complementing the primary colors
            success_color="#4CAF50",  # Green for success messages
            info_color="#29B6F6",  # Light Blue for informational alerts
            warning_color="#FFB300",  # Amber for warnings
            danger_color="#F44336",  # Red for errors and dangerous actions
            background_color="#FAFAFA",  # Very light grey for background, easy on the eyes
            text_color="#37474F",  # Dark Grey for text, ensuring readability
            primary_hover_color="#546E7A",  # Darker shade of primary for hover effects
            secondary_hover_color="#B0BEC5",  # A slightly darker shade of secondary for hover effects
            accent_hover_color="#4DB6AC",  # A darker shade of the accent for hover effects
            success_hover_color="#388E3C",  # Darker green for success hover
            info_hover_color="#039BE5",  # Darker blue for info hover
            warning_hover_color="#FFA000",  # Darker amber for warning hover
            danger_hover_color="#D32F2F",  # Darker red for danger hover
            active=True,
            default=True
        )

        Theme.objects.create(
            name="Refined Dark",
            description="A modern dark mode theme with a focus on depth and consistency. Rich blues and complementary grays create an engaging user experience, enhanced by strategically used accent colors for clarity and focus.",
            primary_color="#455A64",  # Blue Grey for primary components
            secondary_color="#607D8B",  # Lighter Blue Grey for secondary elements
            accent_color="#80CBC4",  # Teal for accents, blending well with the dark theme
            success_color="#4CAF50",  # Green for success indicators
            info_color="#29B6F6",  # Light Blue for informational elements
            warning_color="#FFB300",  # Amber for warning signals
            danger_color="#F44336",  # Red for danger warnings
            background_color="#263238",  # Deep Blue Grey for the background, reducing eye strain
            text_color="#CFD8DC",  # Light Grey for text, offering contrast against the dark background
            primary_hover_color="#37474F",  # A shade darker for primary hover
            secondary_hover_color="#546E7A",  # A shade darker for secondary hover
            accent_hover_color="#4DB6AC",  # A shade darker for accent hover
            success_hover_color="#388E3C",  # A shade darker for success hover
            info_hover_color="#039BE5",  # A shade darker for info hover
            warning_hover_color="#FFA000",  # A shade darker for warning hover
            danger_hover_color="#D32F2F",  # A shade darker for danger hover
            active=True,
            default=False
        )
