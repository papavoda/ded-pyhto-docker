from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from blog.models import Post, AudioInternal, Image, VideoYoutube


# class PostSerializer(serializers.ModelSerializer):
#     audio_internal = serializers.PrimaryKeyRelatedField(many=True, read_only=True, )
#
#     class Meta:
#         fields = (
#             'title',
#             'author',
#             'category',
#             'intro',
#             'main_image',
#             'status',
#             'audio_internal',
#         )
#         model = Post


# class AudioInternalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AudioInternal
#         fields = ('id', 'name', 'post', 'tracknumber', 'track', 'site_play')
#
#     def create(self, validated_data):
#         # Create a new AudioInternal instance
#         audio = AudioInternal(
#             name=validated_data['name'],
#             post=validated_data['post'],
#             tracknumber=validated_data['tracknumber'],
#             track=validated_data['track'],
#             site_play=validated_data['site_play']
#         )
#         audio.save()
#         return audio
#
#     def update(self, instance, validated_data):
#         # Update an existing AudioInternal instance
#         instance.name = validated_data.get('name', instance.name)
#         instance.post = validated_data.get('post', instance.post)
#         instance.tracknumber = validated_data.get('tracknumber', instance.tracknumber)
#         instance.track = validated_data.get('track', instance.track)
#         instance.site_play = validated_data.get('site_play', instance.site_play)
#         instance.save()
#         return instance
class AudioInternalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioInternal
        fields = ('id', 'name', 'tracknumber', 'track', 'site_play')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'name', 'image')


class VideoYoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoYoutube
        fields = ('id', 'name', 'video_frame')


class PostSerializer(serializers.ModelSerializer):
    audio_internal = AudioInternalSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, )
    youtube = VideoYoutubeSerializer(many=True, )

    class Meta:
        model = Post
        fields = ('id', 'title', 'intro', 'text', 'main_image', 'audio_internal', 'images', 'youtube')

    # def create(self, validated_data):
    #     audio_internal_data = validated_data.pop('audio_internal', [])
    #     post = Post.objects.create(**validated_data)
    #     for audio_data in audio_internal_data:
    #         AudioInternal.objects.create(post=post, **audio_data)
    #     return post
    #
    # def update(self, instance, validated_data):
    #     audio_internal_data = validated_data.pop('audio_internal', [])
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.body = validated_data.get('text', instance.body)
    #     instance.save()
    #
    #     # Update or create audio_internal objects
    #     for audio_data in audio_internal_data:
    #         audio_id = audio_data.get('id', None)
    #         if audio_id:
    #             # Update existing audio_internal
    #             audio = AudioInternal.objects.get(id=audio_id)
    #             AudioInternalSerializer(audio, data=audio_data, partial=True).is_valid(raise_exception=True)
    #             AudioInternalSerializer(audio, data=audio_data, partial=True).save()
    #         else:
    #             # Create new audio_internal
    #             AudioInternal.objects.create(post=instance, **audio_data)
    #
    #     # Delete audio_internal objects that were removed
    #     instance.audio_internal.exclude(id__in=[audio_data.get('id', None) for audio_data in audio_internal_data]).delete()
    #
    #     return instance


class PostListSerializer(serializers.ModelSerializer):
    main_image_url = SerializerMethodField('get_main_image')

    def get_main_image(self, instance):
        if instance.main_image:
            return instance.main_image.url

### TODO make main_image as url in list view
    class Meta:
        model = Post
        fields = ('id', 'title', 'intro', 'main_image', 'main_image_url')
