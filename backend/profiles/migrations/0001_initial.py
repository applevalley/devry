# Generated by Django 3.1.5 on 2021-02-19 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumImagePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=80)),
                ('follower_num', models.PositiveIntegerField(default=0)),
                ('followee_num', models.PositiveIntegerField(default=0)),
                ('profile_img', models.URLField(blank=True, default='', max_length=100)),
                ('region', models.CharField(blank=True, max_length=100)),
                ('group', models.CharField(blank=True, default='', max_length=40)),
                ('bio', models.TextField(blank=True, default='')),
                ('sns_name1', models.TextField(blank=True, default='')),
                ('sns_name2', models.TextField(blank=True, default='')),
                ('sns_name3', models.TextField(blank=True, default='')),
                ('sns_url1', models.URLField(blank=True, default='', max_length=100)),
                ('sns_url2', models.URLField(blank=True, default='', max_length=100)),
                ('sns_url3', models.URLField(blank=True, default='', max_length=100)),
                ('tech_stack', multiselectfield.db.fields.MultiSelectField(choices=[('Python3', 'Python3'), ('Django', 'Django'), ('Java', 'Java'), ('Spring', 'Spring'), ('HTML5', 'HTML5'), ('CSS3', 'CSS3'), ('JavaScript', 'JavaScript'), ('TypeScript', 'TypeScript'), ('Vue.js', 'Vue.js'), ('React', 'React'), ('Angular', 'Angular'), ('Node.js', 'Node.js'), ('Swift', 'Swift'), ('Ruby', 'Ruby'), ('Ruby on Rails', 'Ruby on Rails'), ('MySQL', 'MySQL'), ('MariaDB', 'MariaDB'), ('MongoDB', 'MongoDB'), ('Docker', 'Docker'), ('Kubernetes', 'Kubernetes'), ('Frontend', 'Frontend'), ('Backend', 'Backend'), ('DevOps', 'DevOps'), ('Artificial Intelligence', 'Artificial Intelligence'), ('BigData', 'BigData'), ('Blockchain', 'Blockchain'), ('Internet of Things', 'Internet of Things'), ('Augmented Reality', 'Augmented Reality'), ('Virtual Reality', 'Virtual Reality')], max_length=273)),
                ('project_name1', models.CharField(blank=True, default='', max_length=100)),
                ('project_name2', models.CharField(blank=True, default='', max_length=100)),
                ('project_name3', models.CharField(blank=True, default='', max_length=100)),
                ('project_url1', models.URLField(blank=True, default='', max_length=100)),
                ('project_url2', models.URLField(blank=True, default='', max_length=100)),
                ('project_url3', models.URLField(blank=True, default='', max_length=100)),
                ('my_tags', multiselectfield.db.fields.MultiSelectField(choices=[('Python3', 'Python3'), ('Django', 'Django'), ('Java', 'Java'), ('Spring', 'Spring'), ('HTML5', 'HTML5'), ('CSS3', 'CSS3'), ('JavaScript', 'JavaScript'), ('TypeScript', 'TypeScript'), ('Vue.js', 'Vue.js'), ('React', 'React'), ('Angular', 'Angular'), ('Node.js', 'Node.js'), ('Swift', 'Swift'), ('Ruby', 'Ruby'), ('Ruby on Rails', 'Ruby on Rails'), ('MySQL', 'MySQL'), ('MariaDB', 'MariaDB'), ('MongoDB', 'MongoDB'), ('Docker', 'Docker'), ('Kubernetes', 'Kubernetes'), ('Frontend', 'Frontend'), ('Backend', 'Backend'), ('DevOps', 'DevOps'), ('Artificial Intelligence', 'Artificial Intelligence'), ('BigData', 'BigData'), ('Blockchain', 'Blockchain'), ('Internet of Things', 'Internet of Things'), ('Augmented Reality', 'Augmented Reality'), ('Virtual Reality', 'Virtual Reality')], max_length=273)),
                ('pinned_qnas', models.TextField(blank=True)),
                ('pinned_forums', models.TextField(blank=True)),
                ('qnas', models.TextField(blank=True)),
                ('forums', models.TextField(blank=True)),
                ('qnas_comments', models.TextField(blank=True)),
                ('forums_comments', models.TextField(blank=True)),
                ('links', models.TextField()),
                ('projects', models.TextField()),
                ('is_following', models.BooleanField(default=False)),
                ('post_num', models.PositiveIntegerField(default=0)),
                ('joined', models.DateTimeField(blank=True, null=True)),
                ('tags', models.TextField(blank=True)),
                ('link', models.ManyToManyField(blank=True, default=0, related_name='_profile_link_+', to='profiles.Profile')),
                ('project', models.ManyToManyField(blank=True, default=0, related_name='_profile_project_+', to='profiles.Profile')),
                ('thumbnail', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forum_image', to='profiles.forumimagepost')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
