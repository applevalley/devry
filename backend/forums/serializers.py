from rest_framework import serializers, fields
from .models import Post, Comment, tech
from profiles.models import Profile, ForumImagePost
from profiles.serializers import ProfileSerializer, ProfileListSerializer, ProfilePinnedPostsSerializer, ProfileImageSerializer
from accounts.models import User, Mentioned


# class ImgPost(object):
#     def __init__(self, files, thumbnail):
#         self.files = files 
#         self.thumbnail = thumbnail 


# class ImagePostSerializer(serializers.Serializer):
#     files = serializers.FileField()
#     thumbnail = serializers.ImageField()
class ImagePostSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(use_url=True, allow_empty_file = True)
    
    class Meta:
        model = ForumImagePost
        fields = ('thumbnail',)



class UserinfoSerializer(serializers.ModelSerializer):
    profile_img = ProfileImageSerializer(read_only=True)
    class Meta:
        model = User
        fields = ( 'id', 'username', 'profile_img')


class ProfilepostListSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Profile
        fields = ('user', 'username', 'profile_img', )


class ProfileImagePostListSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Profile
        fields = ('id', )


class ProfilepostSerializer(serializers.ModelSerializer):
    pinned_posts = ProfilePinnedPostsSerializer(many=True, read_only=True)
    thumbnail = ImagePostSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ('user', 'username', 'profile_img', 'follower_num', 'bio', 'pinned_posts', 'thumbnail', 'is_following')
# 부족한 필드 추가해야함


class WriterInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('user', )


class ProfilePostSerializer(serializers.ModelSerializer):
    
    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
        )

    class Meta:
        model = Post
        fields = ('id', 'title', 'username', 'written_time', 'thumbnail', 'like_num', 'comment_count', 'ref_tags',)


class PostListforamtSerializer(serializers.ModelSerializer):
    
    user = UserinfoSerializer(
        read_only=True,
    )

    user_info = ProfileImagePostListSerializer(
        read_only=True,
    )
    
    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('id', 'title', 'written_time', 'ref_tags', 'liked', 'comment_count', 'like_num', 'viewed_num',  'user', 'user_info')


class PostListSerializer(serializers.ModelSerializer):
    
    user_info = ProfilepostListSerializer(
        read_only=True,
        many=True
    )
    
    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('id', 'title', 'written_time', 'ref_tags', 'liked', 'comment_count', 'viewed_num', 'like_num', 'user_info',)


class AuthenticatedFeedSerializer(serializers.ModelSerializer):
    feed_list = PostListSerializer(many=True, read_only=True)
    recommend_list = PostListforamtSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('feed_list', 'recommend_list',)


class CommentdetailSerializer(serializers.ModelSerializer):

    profile = ProfilepostListSerializer(
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('id', 'comment_content', 'user','like_comment_num', 'post', 'written_time', 'liked_comment' ,'profile')

 
class CommentlistSerializer(serializers.ModelSerializer):
    
    profile = ProfileListSerializer(
        read_only=True
    )

    user = UserinfoSerializer(
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('id', 'comment_content', 'like_comment_num', 'user', 'post', 'written_time', 'liked_comment' ,'profile')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('user', 'id',  'comment_content', 'like_comment_num', 'post', 'written_time', 'liked_comment', 'profile')


class PostMentionedCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('mentioned',)


class MentionedCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mentioned
        fields = '__all__'


class DetailCommentMentionedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'mentioned', 'mentioned_comment')


class DetailCommentSerializer(serializers.ModelSerializer):
    mentioned = PostMentionedCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = ('user', 'id', 'username', 'profile_img', 'written_time', 'comment_content', 'like_comment_num', 'mentioned')


class MentionedUserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('user','username')


class PostDetailCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('comments',)


class PostSerializer(serializers.ModelSerializer):

    ref_tags= fields.MultipleChoiceField(choices=tech)

    comment_set = CommentSerializer(
        many=True,
        read_only=True,   
    )

    comment_num = serializers.IntegerField(
        source='comment_set.num',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('id','user', 'title','content','ref_tags', 'bookmark_num', 'bookmarked', 'like_num', 'liked',
        'viewed_num', 'comment_num', 'written_time','comment_set', )


class ForumPostSerializer(serializers.ModelSerializer):
    ref_tags= fields.MultipleChoiceField(choices=tech)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'ref_tags', 'bookmark_num', 'bookmarked', 'like_num', 'liked', 'comment_num', 'viewed_num', 'written_time')

class PostdetailSerializer(serializers.ModelSerializer):

    # ref_tags= fields.MultipleChoiceField(choices=tech)
    
    # user = UserinfoSerializer(
    #     read_only=True,
    # )

    writer_info = ProfilepostSerializer(many=True,read_only=True)

    forum_post = ForumPostSerializer(many=True, read_only=True)

    comments = PostDetailCommentSerializer(many=True, read_only=True)
    # comments = PostDetailCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('writer_info', 'forum_post', 'comments')
        # fields = ('id','writer_info', 'title','written_time', 'ref_tags', 'like_num',
        # 'viewed_num', 'bookmark_num','content', 'comment_set', 'liked', 'bookmarked','user' )




class likeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', "liked",  "like_num", "like_users")


class like_commentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id', "liked_comment")


class bookmarkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', "bookmarked",  "bookmark_num", "bookmark_users")


class pinnedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', 'pinned', 'pinned_num', 'pinned_users')


class pinnedDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title',)