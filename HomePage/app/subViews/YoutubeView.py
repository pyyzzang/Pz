from typing import List
from requests import get
import json
from ..module.osDefine import osDefine

from  requests import get;
import json;
import re;


class Format():
    def __init__(self, itag, url, mimeType, bitrate, width, height, lastModified,
     contentLength, quality, qualityLabel, projectionType, averageBitrate,
     audioQuality, approxDurationMs, audioSampleRate, audioChannels):
        self.itag = itag;
        self.url = url;
        self.mimeType = mimeType;
        self.bitrate = bitrate;
        self.width = width;
        self.height = height;
        self.lastModified = lastModified;
        self.contentLength = contentLength;
        self.quality = quality;
        self.qualityLabel = qualityLabel;
        self.projectionType = projectionType;
        self.averageBitrate = averageBitrate
        self.audioQuality = audioQuality;
        self.approxDurationMs = approxDurationMs;
        self.audioSampleRate = audioSampleRate;
        self.audioChannels = audioChannels;

class InitRange():
    def __init__(self, start, end):
        self.start = start;
        self.end = end;

class IndexRange():
    def __init__(self, start, end):
        self.start = start;
        self.end = end;

class ColorInfo():
    def __init__(self, primaries,transferCharacteristics, matrixCoefficients):
        self.primaries = primaries;
        self.transferCharacteristics = transferCharacteristics;
        self.matrixCoefficients = matrixCoefficients;

class AdaptiveFormat():
    def __init__(self, itag, url, mimeType, bitrate, width, height, initRange, indexRange,
    lastModified, contentLength, quality, fps, qualityLabel, projectionType, averageBitrate,
    approxDurationMs, colorInfo, highReplication, audioQuality, audioSampleRate, audioChannels):
        self.itag = itag;
        self.url = url;
        self.mimeType = mimeType;
        self.bitrate = bitrate;
        self.width = width;
        self.height = height;
        self.InitRange = InitRange;
        self.IndexRange = indexRange;
        self.lastModified = lastModified;
        self.contentLength = contentLength;
        self.quality = quality;
        self.fps = fps;
        self.qualityLabel = qualityLabel;
        self.projectionType = projectionType;
        self.averageBitrate = averageBitrate;
        self.approxDurationMs = approxDurationMs;
        self.colorInfo = colorInfo;
        self.highReplication = highReplication;
        self.audioQuality = audioQuality;
        self.audioSampleRate = audioSampleRate;
        self.audioChannels = audioChannels;

class StreamingData():
    def __init__(self, expiresInSeconds, formats, adaptiveFormats):
        self.expiresInSeconds = expiresInSeconds;
        #public List<Format> formats { get; set; }
        self.formats = formats;
        #public List<AdaptiveFormat> adaptiveFormats { get; set; }
        self.adaptiveFormats = adaptiveFormats;

class PlayerAdParams():
    def __init__(self, showContentThumbnail, enabledEngageTypes):
        self.showContentThumbnail = showContentThumbnail;
        self.enabledEngageTypes = enabledEngageTypes;

class GutParams():
    def __init__(self, tag):
        self.tag = tag;

class PlayerLegacyDesktopWatchAdsRenderer():
    def __init__(self, playerAdParams, gutParams, showCompanion, showInstream, useGut):
        self.playerAdParams = playerAdParams ;
        self.gutParams = gutParams;
        self.showCompanion = showCompanion;
        self.showInstream = showInstream;
        self.useGut = useGut;

class PlayerAd():
    def __init__(self, playerLegacyDesktopWatchAdsRenderer):
        self.playerLegacyDesktopWatchAdsRenderer = playerLegacyDesktopWatchAdsRenderer;

class VideostatsPlaybackUrl():
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl;

class VideostatsDelayplayUrl():
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl;

class VideostatsWatchtimeUrl():
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl;

class PtrackingUrl():
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl;

class QoeUrl():
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl;

class SetAwesomeUrl():
    def __init__(self, baseUrl, elapsedMediaTimeSeconds):
        self.baseUrl = baseUrl;
        self.elapsedMediaTimeSeconds = elapsedMediaTimeSeconds;

class AtrUrl():
    def __init__(self, baseUrl, elapsedMediaTimeSeconds):
        self.baseUrl = baseUrl;
        self.elapsedMediaTimeSeconds = elapsedMediaTimeSeconds;

class YoutubeRemarketingUrl():
    def __init__(self, baseUrl, elapsedMediaTimeSeconds):
        self.baseUrl = baseUrl;
        self.elapsedMediaTimeSeconds = elapsedMediaTimeSeconds;

class GoogleRemarketingUrl():
    def __init__(self, baseUrl, elapsedMediaTimeSeconds):
        self.baseUrl = baseUrl;
        self.elapsedMediaTimeSeconds = elapsedMediaTimeSeconds;

class playbackTracking():
    def __init__(self, videostatsPlaybackUrl, videostatsDelayplayUrl, videostatsWatchtimeUrl,
    ptrackingUrl, qoeUrl, setAwesomeUrl, atrUrl, youtubeRemarketingUrl, googleRemarketingUrl):
        self.videostatsPlaybackUrl = videostatsPlaybackUrl;
        self.videostatsDelayplayUrl = videostatsDelayplayUrl;
        self.videostatsWatchtimeUrl = videostatsWatchtimeUrl;
        self.ptrackingUrl = ptrackingUrl;
        self.qoeUrl = qoeUrl;
        self.setAwesomeUrl = setAwesomeUrl;
        self.atrUrl = atrUrl;
        self.youtubeRemarketingUrl = youtubeRemarketingUrl;
        self.googleRemarketingUrl = googleRemarketingUrl;

class WebCommandMetadata():
    def __init__(self, url, rootVe):
        self.url = url;
        self.rootVe = rootVe;

class CommandMetadata():
    def __init__(self, webCommandMetadata):
        self.webCommandMetadata = webCommandMetadata;

class UrlEndpoint():
    def __init__(self, url):
        self.url = url;

class NavigationEndpoint():
    def __init__(self, clickTrackingParams, commandMetadata, urlEndpoint):
        self.clickTrackingParams = clickTrackingParams;
        self.commandMetadata = commandMetadata;
        self.urlEndpoint = urlEndpoint;

class Run():
    def __init__(self, text, navigationEndpoint):
        self.text = text;
        self.navigationEndpoint = navigationEndpoint;

class AddSubtitlesText():
    def __init__(self, runs):
        #public List<Run> runs { get; set; }
        self.runs = runs;

class NoSubtitlesText():
    def __init__(self, simpleText):
        self.simpleText = simpleText;

class PromoSubtitlesText():
    def __init__(self, simpleText):
        self.simpleText = simpleText;

class CaptionsMetadataRenderer():
    def __init__(self, addSubtitlesText, noSubtitlesText, promoSubtitlesText):
        self.addSubtitlesText = addSubtitlesText;
        self.noSubtitlesText = noSubtitlesText;
        self.promoSubtitlesText = promoSubtitlesText;

class Contribute():
    def __init__(self, captionsMetadataRenderer):
        self.captionsMetadataRenderer = captionsMetadataRenderer;

class PlayerCaptionsRenderer():
    def __init__(self, baseUrl, visibility, contribute):
        self.baseUrl = baseUrl;
        self.visibility = visibility;
        self.contribute = contribute;

class Name():
    def __init__(self, simpleText):
        self.simpleText = simpleText;

class CaptionTrack():
    def __init__(self, baseUrl, name, vssId, languageCode, isTranslatable):
        self.baseUrl = baseUrl;
        self.name = name;
        self.vssId = vssId;
        self.languageCode = languageCode;
        self.isTranslatable = isTranslatable;

class AudioTrack():
    def __init__(self, captionTrackIndices):
        #public List<int> captionTrackIndices { get; set; }
        self.captionTrackIndices = captionTrackIndices;

class LanguageName():
    def __init__(self, simpleText):
        self.simpleText = simpleText;

class TranslationLanguage():
    def __init__(self, languageCode, languageName):
        self.languageCode = languageCode;
        #public LanguageName languageName { get; set; }
        self.languageName = languageName;

class WebCommandMetadata2():
    def __init__(self, url, rootVe):
        self.url = url;
        self.rootVe = rootVe;

class CommandMetadata2():
    def __init__(self, webCommandMetadata):
        #public WebCommandMetadata2 webCommandMetadata { get; set; }
        self.webCommandMetadata = webCommandMetadata;

class UrlEndpoint2():
    def __init__(self, url):
        self.url = url;

class NavigationEndpoint2():
    def __init__(self, clickTrackingParams, commandMetadata, urlEndpoint):
        self.clickTrackingParams = clickTrackingParams;
        #public CommandMetadata2 commandMetadata { get; set; }
        self.commandMetadata = commandMetadata;
        #public UrlEndpoint2 urlEndpoint { get; set; }
        self.urlEndpoint = urlEndpoint;

class Run2():
    def __init__(self, text, navigationEndpoint):
        self.text = text;
        #public NavigationEndpoint2 navigationEndpoint { get; set; }
        self.navigationEndpoint = navigationEndpoint;

class AddSubtitlesText2():
    def __init__(self, runs):
        #public List<Run2> runs { get; set; }
        self.runs = runs;

class NoSubtitlesText2():
    def __init__(self, simpleText):
        self.simpleText = simpleText;

class PromoSubtitlesText2():
    def __init__(self, simpleText):
        self.simpleText = simpleText;

class CaptionsMetadataRenderer2():
    def __init__(self, addSubtitlesText, noSubtitlesText, promoSubtitlesText):
        #public AddSubtitlesText2 addSubtitlesText { get; set; }
        self.addSubtitlesText = addSubtitlesText;
        #public NoSubtitlesText2 noSubtitlesText { get; set; }
        self.noSubtitlesText = noSubtitlesText;
        #public PromoSubtitlesText2 promoSubtitlesText { get; set; }
        self.promoSubtitlesText = promoSubtitlesText;

class Contribute2():
    def __init__(self, captionsMetadataRenderer):
        #public CaptionsMetadataRenderer2 captionsMetadataRenderer { get; set; }
        self.captionsMetadataRenderer = captionsMetadataRenderer;

class PlayerCaptionsTracklistRenderer():
    def __init__(self, captionTracks, audioTracks, translationLanguages, defaultAudioTrackIndex, contribute):
        #public List<CaptionTrack> captionTracks { get; set; }
        self.captionTracks = captionTracks;
        #public List<AudioTrack> audioTracks { get; set; }
        self.audioTracks = audioTracks;
        #public List<TranslationLanguage> translationLanguages { get; set; }
        self.translationLanguages = translationLanguages;
        self.defaultAudioTrackIndex = defaultAudioTrackIndex;
        #public Contribute2 contribute { get; set; }
        self.contribute = contribute;

class Captions():
    def __init__(self, playerCaptionsRenderer, playerCaptionsTracklistRenderer):
        #public PlayerCaptionsRenderer playerCaptionsRenderer { get; set; }
        self.playerCaptionsRenderer = playerCaptionsRenderer;
        #public PlayerCaptionsTracklistRenderer playerCaptionsTracklistRenderer { get; set; }
        self.playerCaptionsTracklistRenderer = playerCaptionsTracklistRenderer;

class Thumbnail2():
    def __init__(self, url, width, height):
        self.url = url;
        self.width = width;
        self.height = height;

class Thumbnail():
    def __init__(self, thumbnails):
        #public List<Thumbnail2> thumbnails { get; set; }
        self.thumbnails = thumbnails;

class VideoDetails():
    def __init__(self, videoId, title, lengthSeconds, keywords, channelId, isOwnerViewing,
    shortDescription, isCrawlable, thumbnail, averageRating, allowRatings, viewCount,
    author, isPrivate, isUnpluggedCorpus, isLiveContent):
        self.videoId = videoId;
        self.title = title;
        self.lengthSeconds = lengthSeconds;
        #public List<string> keywords { get; set; }
        self.keywords = keywords;
        self.channelId = channelId;
        self.isOwnerViewing = isOwnerViewing;
        self.shortDescription = shortDescription;
        self.isCrawlable = isCrawlable;
        #public Thumbnail thumbnail { get; set; }
        self.thumbnail = thumbnail;
        self.averageRating = averageRating;
        self.allowRatings = allowRatings;
        self.viewCount = viewCount;
        self.author = author;
        self.isPrivate = isPrivate;
        self.isUnpluggedCorpus = isUnpluggedCorpus;
        self.isLiveContent = isLiveContent;

class Thumbnail3():
    def __init__(self, url, width, height):
        self.url = url;
        self.width = width;
        self.height = height;

class Watermark():
    def __init__(self, thumbnails):
        #public List<Thumbnail3> thumbnails { get; set; }
        self.thumbnails = thumbnails;

class WebCommandMetadata3():
    def __init__(self, url, webPageType, rootVe):
        self.url = url;
        self.webPageType = webPageType;
        self.rootVe = rootVe;

class CommandMetadata3():
    def __init__(self, webCommandMetadata):
        #public WebCommandMetadata3 webCommandMetadata { get; set; }
        self.webCommandMetadata = webCommandMetadata;

class BrowseEndpoint():
    def __init__(self, browseId):
        self.browseId = browseId;

class NavigationEndpoint3():
    def __init__(self, clickTrackingParams, commandMetadata, browseEndpoint):
        #public string clickTrackingParams { get; set; }
        self.clickTrackingParams = clickTrackingParams;
        self.commandMetadata = commandMetadata;
        self.browseEndpoint = browseEndpoint;

class Run3():
    def __init__(self, text):
        self.text = text;

class ButtonText():
    def __init__(self, runs):
        #public List<Run3> runs { get; set; }
        self.runs = runs;

class Run4():
    def __init__(self, text):
        self.text = text;

class SubscribedButtonText():
    def __init__(self, runs):
        #public List<Run4> runs { get; set; }
        self.runs = runs;

class Run5():
    def __init__(self, text):
        self.text = text;

class UnsubscribedButtonText():
    def __init__(self, runs):
        #public List<Run5> runs { get; set; }
        self.runs = runs;

class Run6():
    def __init__(self, text):
        self.text = text;

class UnsubscribeButtonText():
    def __init__(self, runs):
        #public List<Run6> runs { get; set; }
        self.runs = runs;

class WebCommandMetadata4():
    def __init__(self, url, sendPost, apiUrl):
        self.url = url;
        self.sendPost = sendPost;
        self.apiUrl = apiUrl;

class CommandMetadata4():
    def __init__(self, webCommandMetadata):
        #public WebCommandMetadata4 webCommandMetadata { get; set; }
        self.webCommandMetadata = webCommandMetadata;

class SubscribeEndpoint():
    def __init__(self, channelIds, params):
        #public List<string> channelIds { get; set; };
        self.channelIds = channelIds;
        self.params = params;

class UnsubscribeEndpoint():
    def __init__(self, channelIds, params):
        #public List<string> channelIds { get; set; }
        self.channelIds = channelIds;
        self.params = params;

class ServiceEndpoint():
    def __init__(self, clickTrackingParams, commandMetadata, 
    subscribeEndpoint, unsubscribeEndpoint):
        self.clickTrackingParams = clickTrackingParams;
        #public CommandMetadata4 commandMetadata { get; set; }
        self.commandMetadata = commandMetadata;
        #public SubscribeEndpoint subscribeEndpoint { get; set; }
        self.subscribeEndpoint = subscribeEndpoint;
        #public UnsubscribeEndpoint unsubscribeEndpoint { get; set; }
        self.unsubscribeEndpoint = unsubscribeEndpoint;

class WebCommandMetadata5():
    def __init__(self):
        self.empty = "";

class CommandMetadata5():
    def __init__(self):
        #public WebCommandMetadata5 webCommandMetadata { get; set; }
        self.webCommandMetadata = webCommandMetadata;

class WebNavigationEndpointData():
    def __init__(self, url):
        self.url = url

class SignInEndpoint():
    def __init__(self, clickTrackingParams, commandMetadata, webNavigationEndpointData):
        self.clickTrackingParams = clickTrackingParams;
        #public CommandMetadata5 commandMetadata { get; set; }
        self.commandMetadata = commandMetadata;
        #public WebNavigationEndpointData webNavigationEndpointData { get; set; }
        self.webNavigationEndpointData = webNavigationEndpointData;

class SubscribeButtonRenderer():
    def __init__(self, buttonText, subscribed, enabled, type, channelId, showPreferences,
    subscribedButtonText, unsubscribedButtonText, trackingParams, unsubscribeButtonText,
    serviceEndpoints, signInEndpoint):
        #public ButtonText buttonText { get; set; }
        self.buttonText = buttonText;
        self.subscribed = subscribed;
        self.enabled = enabled;
        self.type = type;
        self.channelId = channelId;
        self.showPreferences = showPreferences;
        #public SubscribedButtonText subscribedButtonText { get; set; }
        self.subscribedButtonText = subscribedButtonText;
        #public UnsubscribedButtonText unsubscribedButtonText { get; set; }
        self.unsubscribedButtonText = unsubscribedButtonText;
        self.trackingParams = trackingParams;
        #public UnsubscribeButtonText unsubscribeButtonText { get; set; }
        self.unsubscribeButtonText = unsubscribeButtonText;
        #public List<ServiceEndpoint> serviceEndpoints { get; set; }
        self.serviceEndpoints = serviceEndpoints;
        #public SignInEndpoint signInEndpoint { get; set; }
        self.signInEndpoint = signInEndpoint;

class SubscribeButton():
    def __init__(self, subscribeButtonRenderer):
        #public SubscribeButtonRenderer subscribeButtonRenderer { get; set; }
        self.subscribeButtonRenderer = subscribeButtonRenderer;

class FeaturedChannel():
    def __init__(self, startTimeMs, endTimeMs, watermark, trackingParams,
    navigationEndpoint, channelName, subscribeButton):
        self.startTimeMs = startTimeMs;
        self.endTimeMs = endTimeMs;
        #public Watermark watermark { get; set; }
        self.watermark = watermark;
        self.trackingParams = trackingParams;
        #public NavigationEndpoint3 navigationEndpoint { get; set; }
        self.navigationEndpoint = navigationEndpoint;
        self.channelName = channelName;
        #public SubscribeButton subscribeButton { get; set; }
        self.subscribeButton = subscribeButton;

class PlayerAnnotationsExpandedRenderer():
    def __init__(self, featuredChannel, allowSwipeDismiss, annotationId):
        #public FeaturedChannel featuredChannel { get; set; }
        self.featuredChannel = featuredChannel;
        self.allowSwipeDismiss = allowSwipeDismiss;
        self.annotationId = annotationId;

class Annotation():
    def __init__(self, playerAnnotationsExpandedRenderer):
        #public PlayerAnnotationsExpandedRenderer playerAnnotationsExpandedRenderer { get; set; }
        self.playerAnnotationsExpandedRenderer = playerAnnotationsExpandedRenderer;

class AudioConfig():
    def __init__(self, loudnessDb, perceptualLoudnessDb, enablePerFormatLoudness):
        self.loudnessDb = loudnessDb;
        self.perceptualLoudnessDb = perceptualLoudnessDb;
        self.enablePerFormatLoudness = enablePerFormatLoudness;

class StreamSelectionConfig():
    def __init__(self, maxBitrate):
        self.maxBitrate = maxBitrate;

class DynamicReadaheadConfig():
    def __init__(self, maxReadAheadMediaTimeMs, minReadAheadMediaTimeMs, readAheadGrowthRateMs):
        self.maxReadAheadMediaTimeMs = maxReadAheadMediaTimeMs;
        self.minReadAheadMediaTimeMs = minReadAheadMediaTimeMs;
        self.readAheadGrowthRateMs = readAheadGrowthRateMs;

class MediaCommonConfig():
    def __init__(self, dynamicReadaheadConfig):
        #public DynamicReadaheadConfig dynamicReadaheadConfig { get; set; }
        self.dynamicReadaheadConfig = dynamicReadaheadConfig;

class PlayerConfig():
    def __init__(self, audioConfig, streamSelectionConfig, mediaCommonConfig):
        #public AudioConfig audioConfig { get; set; }
        self.audioConfig = audioConfig;
        #public StreamSelectionConfig streamSelectionConfig { get; set; }
        self.streamSelectionConfig = streamSelectionConfig;
        #public MediaCommonConfig mediaCommonConfig { get; set; }
        self.mediaCommonConfig = mediaCommonConfig;

class PlayerStoryboardSpecRenderer():
    def __init__(self, spec):
        self.spec = spec;

class Storyboards():
    def __init__(self, playerStoryboardSpecRenderer):
        #public PlayerStoryboardSpecRenderer playerStoryboardSpecRenderer { get; set; }
        self.playerStoryboardSpecRenderer = playerStoryboardSpecRenderer;

class Thumbnail5():
    def __init__(self, url, width, height):
        self.url = url;
        self.width = width;
        self.height = height;

class Thumbnail4():
    def __init__(self, thumbnails):
        #public List<Thumbnail5> thumbnails { get; set; }
        self.thumbnails = thumbnails;

class Embed():
    def __init__(self, iframeUrl, flashUrl, width, height, flashSecureUrl):
        self.iframeUrl = iframeUrl;
        self.flashUrl = flashUrl;
        self.width = width;
        self.height = height;
        self.flashSecureUrl = flashSecureUrl;

class Title():
    def __init__(self, simpleText):
        self.simpleText = simpleText;

class Description():
    def __init__(self, simpletext):
        self.simpletext = simpletext;

class PlayerMicroformatRenderer():
    def __init__(self, thumbnail, embed, title, description, lengthSeconds, ownerProfileUrl,
    ownerGplusProfileUrl, externalChannelId, isFamilySafe, availableCountries, isUnlisted,
    hasYpcMetadata, viewCount, category, publishDate, ownerChannelName, uploadDate):
        #public Thumbnail4 thumbnail { get; set; }
        self.thumbnail = thumbnail;
        #public Embed embed { get; set; }
        self.embed = embed;
        #public Title title { get; set; }
        self.title = title;
        #public Description description { get; set; }
        self.description = description;
        self.lengthSeconds = lengthSeconds;
        self.ownerProfileUrl = ownerProfileUrl;
        self.ownerGplusProfileUrl = ownerGplusProfileUrl;
        self.externalChannelId = externalChannelId;
        self.isFamilySafe = isFamilySafe;
        #public List<string> availableCountries { get; set; }
        self.availableCountries = availableCountries;
        self.isUnlisted = isUnlisted;
        self.hasYpcMetadata = hasYpcMetadata;
        self.viewCount = viewCount;
        self.category = category;
        self.publishDate = publishDate;
        self.ownerChannelName = ownerChannelName;
        self.uploadDate = uploadDate;

class Microformat():
    def __init__(self, playerMicroformatRenderer):
        #public PlayerMicroformatRenderer playerMicroformatRenderer { get; set; }
        self.playerMicroformatRenderer = playerMicroformatRenderer;

class Message():
    def __init__(self, simpleText):
        self.simpleText = simpleText;

class SimpleCardTeaserRenderer():
    def __init__(self, message, trackingParams, prominent, logVisibilityUpdates):
        #public Message message { get; set; }
        self.message = message;
        self.trackingParams = trackingParams;
        self.prominent = prominent;
        self.logVisibilityUpdates = logVisibilityUpdates;

class Teaser():
    def __init__(self, simpleCardTeaserRenderer):
        #public SimpleCardTeaserRenderer simpleCardTeaserRenderer { get; set; }
        self.simpleCardTeaserRenderer = simpleCardTeaserRenderer;

class Thumbnail6():
    def __init__(self, url, whdti, height):
        self.url = url;
        self.width = width;
        self.heigth = heigth;

class VideoThumbnail():
    def __init__(self, thumbnails):
        #public List<Thumbnail6> thumbnails { get; set; }
        self.thumbnails = thumbnails;

class AccessibilityData():
    def __init__(self, label):
        self.label = label;

class Accessibility():
    def __init__(self, accessibilityData):
        #public AccessibilityData accessibilityData { get; set; }
        self.accessibilityData = accessibilityData;

class LengthString():
    def __init__(self, accessibility, simpleText):
        #public Accessibility accessibility { get; set; }
        self.accessibility = accessibility;
        self.simpleText = simpleText;

class VideoTitle():
    def __init__(self, simpleText):
        self.simpleText = simpleText;

class ChannelName():
    def __init__(self, simpleText):
        self.simpleText = simpleText;

class ViewCountText():
    def __init__(self, simpleText):
        self.simpleText = simpleText;

class WebCommandMetadata6():
    def __init__(self, url, webPageType, rootVe):
        self.url = url;
        self.webPageType = webPageType;
        self.rootVe = rootVe;

class CommandMetadata6():
    def __init__(self, webCommandMetadata):
        #public WebCommandMetadata6 webCommandMetadata { get; set; }
        self.webCommandMetadata = webCommandMetadata;

class WatchEndpoint():
    def __init__(self, videoId):
        self.videoId = videoId;

class Action():
    def __init__(self, clickTrackingParams, commandMetadata, watchEndpoint):
        self.clickTrackingParams = clickTrackingParams;
        #public CommandMetadata6 commandMetadata { get; set; }
        self.commandMetadata = commandMetadata;
        self.watchEndpoint = watchEndpoint;

class VideoInfoCardContentRenderer():
    def __init__(self, videoThumbnail, lengthString, videoTitle, channelName,
    viewCountText, action, trackingParams):
        #public VideoThumbnail videoThumbnail { get; set; }
        self.videoThumbnail = videoThumbnail;
        #public LengthString lengthString { get; set; }
        self.lengthString = lengthString;
        #public VideoTitle videoTitle { get; set; }
        self.videoTitle = videoTitle;
        #public ChannelName channelName { get; set; }
        self.channelName = channelName;
        #public ViewCountText viewCountText { get; set; }
        self.viewCountText = viewCountText;
        #public Action action { get; set; }
        self.action = action;
        self.trackingParams = trackingParams;

class Content():
    def __init__(self, videoInfoCardContentRenderer):
        #public VideoInfoCardContentRenderer videoInfoCardContentRenderer { get; set; }
        self.videoInfoCardContentRenderer = videoInfoCardContentRenderer;

class CueRange():
    def __init__(self, startCardActiveMs, endCardActiveMs, teaserDurationMs, iconAfterTeaserMs):
        self.startCardActiveMs = startCardActiveMs;
        self.endCardActiveMs = endCardActiveMs;
        self.teaserDurationMs = teaserDurationMs;
        self.iconAfterTeaserMs = iconAfterTeaserMs;

class InfoCardIconRenderer():
    def __init__(self, trackingParams):
        self.trackingParams = trackingParams;

class Icon():
    def __init__(self, infoCardIconRenderer):
        #public InfoCardIconRenderer infoCardIconRenderer { get; set; }
        self.infoCardIconRenderer = infoCardIconRenderer;

class CardRenderer():
    def __init__(self, teaser, content, cueRanges, icon, trackingParams, cardId, feature):
        #public Teaser teaser { get; set; }
        self.teaser = teaser;
        #public Content content { get; set; }
        self.content = content;
        #public List<CueRange> cueRanges { get; set; }
        self.cueRanges = cueRanges;
        #public Icon icon { get; set; }
        self.icon = icon;
        self.trackingParams = trackingParams;
        self.cardId = cardId;
        self.feature = feature;

class Card():
    def __init__(self, cardRenderer):
        #public CardRenderer cardRenderer { get; set; }
        self.cardRenderer = cardRenderer;

class HeaderText():
    def __init__(self, simpleText):
        self.simpleText = simpleText;

class InfoCardIconRenderer2():
    def __init__(self, trackingParams):
        self.trackingParams = trackingParams;

class Icon2():
    def __init__(self, infoCardIconRenderer):
        #public InfoCardIconRenderer2 infoCardIconRenderer { get; set; }
        self.infoCardIconRenderer = infoCardIconRenderer;

class InfoCardIconRenderer3():
    def __init__(self, trackingParams):
        self.trackingParams = trackingParams;

class CloseButton():
    def __init__(self, infoCardIconRenderer):
        #public InfoCardIconRenderer3 infoCardIconRenderer { get; set; }
        self.infoCardIconRenderer = infoCardIconRenderer;

class CardCollectionRenderer():
    def __init__(self, cards, headerText, icon, closeButton, 
    trackingParams, allowTeaserDismiss, logIconVisibilityUpdates):
        #public List<Card> cards { get; set; }
        self.cards = cards;
        #public HeaderText headerText { get; set; }
        self.headerText = headerText;
        #public Icon2 icon { get; set; }
        self.icon = icon;
        #public CloseButton closeButton { get; set; }
        self.closeButton = closeButton;
        self.trackingParams = trackingParams;
        self.allowTeaserDismiss = allowTeaserDismiss;
        self.logIconVisibilityUpdates = logIconVisibilityUpdates;

class Cards():
    def __init__(self, cardCollectionRenderer):
        #public CardCollectionRenderer cardCollectionRenderer { get; set; }
        self.cardCollectionRenderer = cardCollectionRenderer;

class BotguardData():
    def __init__(self, program, interpreterUrl):
        self.program = program;
        self.interpreterUrl = interpreterUrl;

class PlayerAttestationRenderer():
    def __init__(self, challenge, botguardData):
        self.challenge = challenge;
        #public BotguardData botguardData { get; set; }
        self.botguardData = botguardData;

class Attestation():
    def __init__(self, playerAttestationRenderer):
        #public PlayerAttestationRenderer playerAttestationRenderer { get; set; }
        self.playerAttestationRenderer = playerAttestationRenderer;

class TriggerCriteria():
    def __init__(self, connectionWhitelists, joinLatencySeconds, rebufferTimeSeconds,
    watchTimeWindowSeconds, refractorySeconds):
        #public List<string> connectionWhitelists { get; set; }
        self.connectionWhitelists = connectionWhitelists;
        self.joinLatencySeconds = joinLatencySeconds;
        self.rebufferTimeSeconds = rebufferTimeSeconds;
        self.watchTimeWindowSeconds = watchTimeWindowSeconds;
        self.refractorySeconds = refractorySeconds;

class Run7():
    def __init__(self, text, bold):
        self.text = text;
        self.bold = bold;

class Text():
    def __init__(self, runs):
        #public List<Run7> runs { get; set; }
        self.runs = runs;

class WebCommandMetadata7():
    def __init__(self, url, rootVe):
        self.url = url;
        self.rootVe = rootVe;

class CommandMetadata7():
    def __init__(self, webCommandMetadata):
        #public WebCommandMetadata7 webCommandMetadata { get; set; }
        self.webCommandMetadata = webCommandMetadata;

class UrlEndpoint3():
    def __init__(self, url, target):
        self.url = url;
        self.target = target;

class Endpoint():
    def __init__(self, clickTrackingParams, commandMetadata, urlEndpoint):
        self.clickTrackingParams = clickTrackingParams;
        #public CommandMetadata7 commandMetadata { get; set; }
        self.commandMetadata = commandMetadata;
        #public UrlEndpoint3 urlEndpoint { get; set; }
        self.urlEndpoint = urlEndpoint;

class VideoQualityPromoCloseRenderer():
    def __init__(self, trackingParams):
        self.trackingParams = trackingParams;

class CloseButton2():
    def __init__(self, videoQualityPromoCloseRenderer):
        #public VideoQualityPromoCloseRenderer videoQualityPromoCloseRenderer { get; set; }
        self.videoQualityPromoCloseRenderer = videoQualityPromoCloseRenderer;

class VideoQualityPromoRenderer():
    def __init__(self, triggerCriteria, text, endpoint, trackingParams, closeButton):
        #public TriggerCriteria triggerCriteria { get; set; }
        self.triggerCriteria = triggerCriteria;
        #public Text text { get; set; }
        self.text = text;
        #public Endpoint endpoint { get; set; }
        self.endpoint = endpoint;
        self.trackingParams = trackingParams;
        #public CloseButton2 closeButton { get; set; }
        self.closeButton = closeButton;

class VideoQualityPromoSupportedRenderers():
    def __init__(self, videoQualityPromoRenderer):
        #public VideoQualityPromoRenderer videoQualityPromoRenderer { get; set; }
        self.videoQualityPromoRenderer = videoQualityPromoRenderer;

class Run8():
    def __init__(self, text):
        self.text = text;

class MessageText():
    def __init__(self, runs):
        #public List<Run8> runs { get; set; }
        self.runs = runs;

class Run9():
    def __init__(self,text):
        self.text = text;

class Text2():
    def __init__(self, runs):
        #public List<Run9> runs { get; set; }
        self.runs = runs;

class WebCommandMetadata8():
    def __init__(self, url, webPageType, rootVe):
        self.url = url;
        self.webPageType = webPageType;
        self.rootVe = rootVe;

class CommandMetadata8():
    def __init__(self, webCommandMetadata):
        #public WebCommandMetadata8 webCommandMetadata { get; set; }
        self.webCommandMetadata = webCommandMetadata;

class BrowseEndpoint2():
    def __init__(self, browseId, params):
        self.browseId = browseId;
        #public string @params { get; set; }
        self.params = params;

class NavigationEndpoint4():
    def __init__(self, clickTrackingParams, commandMetadata, browseEndpoint):
        self.clickTrackingParams = clickTrackingParams;
        #public CommandMetadata8 commandMetadata { get; set; }
        self.commandMetadata = commandMetadata;
        #public BrowseEndpoint2 browseEndpoint { get; set; }
        self.browseEndpoint = browseEndpoint

class ButtonRenderer():
    def __init__(self, style, size, text, navigationEndpoint, trackingParams):
        self.style = style;
        self.size = size;
        #public Text2 text { get; set; }
        self.text = text;
        #public NavigationEndpoint4 navigationEndpoint { get; set; }
        self.navigationEndpoint = navigationEndpoint;
        self.trackingParams = trackingParams;

class ActionButton():
    def __init__(self, buttonRenderer):
        #public ButtonRenderer buttonRenderer { get; set; }
        self.buttonRenderer = buttonRenderer;

class Run10():
    def __init__(self, text):
        self.text = text;

class Text3():
    def __init__(self, runs):
        #public List<Run10> runs { get; set; }
        self.runs = runs;

class WebCommandMetadata9():
    def __init__(self, url, sendPost, apiUrl):
        self.url = url;
        self.sendPost = sendPost;
        self.apiUrl = apiUrl;

class CommandMetadata9():
    def __init__(self, webCommandMetadata):
        #public WebCommandMetadata9 webCommandMetadata { get; set; }
        self.webCommandMetadata = webCommandMetadata;

class UiActions():
    def __init__(self, hideEnclosingContainer):
        self.hideEnclosingContainer = hideEnclosingContainer;

class FeedbackEndpoint():
    def __init__(self, feedbackToken, uiActions):
        self.feedbackToken = feedbackToken;
        #public UiActions uiActions { get; set; }
        self.uiActions = uiActions;

class ServiceEndpoint2():
    def __init__(self, clickTrackingParams, commandMetadata, feedbackEndpoint):
        self.clickTrackingParams = clickTrackingParams;
        #public CommandMetadata9 commandMetadata { get; set; }
        self.commandMetadata = commandMetadata;
        #public FeedbackEndpoint feedbackEndpoint { get; set; }
        self.feedbackEndpoint = feedbackEndpoint;

class ButtonRenderer2():
    def __init__(self, style, size, text, serviceEndPoint, trackingParams):
        self.style = style;
        self.size = size;
        #public Text3 text { get; set; }
        self.text = text;
        #public ServiceEndpoint2 serviceEndpoint { get; set; }
        self.serviceEndpoint = serviceEndpoint;
        self.trackingParams = trackingParams;

class DismissButton():
    def __init__(self, buttonRenderer):
        #public ButtonRenderer2 buttonRenderer { get; set; }
        self.buttonRenderer = buttonRenderer;

class WebCommandMetadata10():
    def __init__(self, url, sendPost, apiUrl):
        self.url = url;
        self.sendPost = sendPost;
        self. apiUrl = apiUrl;

class CommandMetadata10():
    def __init__(self, webCommandMetadata):
        #public WebCommandMetadata10 webCommandMetadata { get; set; }
        self.webCommandMetadata = webCommandMetadata;

class UiActions2():
    def __init__(self, hideEnclosingContainer):
        self.hideEnclosingContainer = hideEnclosingContainer;

class FeedbackEndpoint2():
    def __init__(self, feedbackToken, uiActions):
        self.feedbackToken = feedbackToken;
        #public UiActions2 uiActions { get; set; }
        self.uiActions = uiActions;

class ImpressionEndpoint():
    def __init__(self, clickTrackingParams, commandMetadata, feedbackEndpoint):
        self.clickTrackingParams = clickTrackingParams;
        #public CommandMetadata10 commandMetadata { get; set; }
        self.commandMetadata = commandMetadata;
        #public FeedbackEndpoint2 feedbackEndpoint { get; set; }
        self.feedbackEndpoint = feedbackEndpoint;

class Run11():
    def __init__(self, text):
        self.text = text;

class MessageTitle():
    def __init__(self, runs):
        #public List<Run11> runs { get; set; }
        self.runs = runs;

class MealbarPromoRenderer():
    def __init__(self, messageTexts, actionButton, dismissButton, triggerCondition,
    style, trackingParams, impressionEndpoints, isVisible, messageTitle):
        #public List<MessageText> messageTexts { get; set; }
        self.messageTexts = messageTexts;
        #public ActionButton actionButton { get; set; }
        self.actionButton = actionButton;
        #public DismissButton dismissButton { get; set; }
        self.dismissButton = dismissButton;
        self.triggerCondition = triggerCondition;
        self.style = style;
        self.trackingParams = trackingParams;
        #public List<ImpressionEndpoint> impressionEndpoints { get; set; }
        self.impressionEndpoints = impressionEndpoints;
        self.isVisible = isVisible;
        #public MessageTitle messageTitle { get; set; }
        self.messageTitle = messageTitle;

class Messages():
    def __init__(self, mealbarPromoRenderer):
        #public MealbarPromoRenderer mealbarPromoRenderer { get; set; }
        self.mealbarPromoRenderer = mealbarPromoRenderer;

class AdPlacements():
    def __init__(self, adPlacementRenderer):
        #public AdPlacementRenderer adPlacementRenderer { get; set; }
        self.adPlacementRenderer = adPlacementRenderer;

class PlayabilityStatus():
	def __init__(self, status, playableInEmbed, contextParams):
		self.status = status;
		self.playableInEmbed = playableInEmbed;
		self.contextParams = contextParams;

class PlayerResponse():
    def __init__(self, playabilityStatus, streamingData, playerAds, playbackTracking,
    captions, videoDetails, annotations, playerConfig, storyboards, microformat,
    cards, trackingParams, attestation, videoQualityPromoSupportedRenderers, messages, adPlacements):
        #public PlayabilityStatus playabilityStatus { get; set; }
        self.playabilityStatus = playabilityStatus;
        #public StreamingData streamingData { get; set; }
        self.streamingData = streamingData;
        #public List<PlayerAd> playerAds { get; set; }
        self.playerAds = playerAds;
        #public PlaybackTracking playbackTracking { get; set; }
        self.playbackTracking = playbackTracking;
        #public Captions captions { get; set; }
        self.captions = captions;
        #public VideoDetails videoDetails { get; set; }
        self.videoDetails = videoDetails;
        #public List<Annotation> annotations { get; set; }
        self.annotations = annotations;
        #public PlayerConfig playerConfig { get; set; }
        self.playerConfig = playerConfig;
        #public Storyboards storyboards { get; set; }
        self.storyboards = storyboards;
        #public Microformat microformat { get; set; }
        self.microformat = microformat;
        #public Cards cards { get; set; }
        self.cards = cards;
        self.trackingParams = trackingParams;
        #public Attestation attestation { get; set; }
        self.attestation = attestation;
        #public VideoQualityPromoSupportedRenderers videoQualityPromoSupportedRenderers { get; set; }
        self.videoQualityPromoSupportedRenderers = videoQualityPromoSupportedRenderers;
        #public List<Message2> messages { get; set; }
        self.messages = messages;
        #public List<AdPlacement> adPlacements { get; set; }
        self.adPlacements = adPlacements;

class RootObject():
    def __init__(self, player_response):
        #public PlayerResponse player_response { get; set; }
        self.player_response = player_response;

class Assets():
    def __init__(self, css, js):
        self.css = css;
        self.js = js

class Attrs():
    def __init__(self, id):
        self.id = id;

class Args():
    def __init__(self, enablecsi, gapi_hint_params, innertube_params, innertube_context_client_version,
     cver, vss_host, csi_page_type, c, hl, cr, enablejsapi, innertube_api_version,
      watermark, loaderUrl, innertube_api_key, fflags, host_language, player_response, fexp):
        self.enablecsi = enablecsi;
        self.gapi_hint_params =gapi_hint_params;
        self.innertube_context_client_version = innertube_context_client_version;
        self.cver = cver;
        self.vss_host = vss_host;
        self.csi_page_type = csi_page_type;
        self.c = c;
        self.hl = hl;
        self.cr = cr;
        self.enablejsapi = enablejsapi;
        self.innertube_api_version = innertube_api_version;
        self.watermark = watermark;
        self.loaderUrl = loaderUrl;
        self.innertube_api_key = innertube_api_key;
        self.fflags = fflags;
        self.host_language = host_language;
        self.player_response = player_response;
        self.fexp = fexp;

class AdPlacementRenderer():
    def __init__(self, config, renderer, trackingParams):
            #public Config config { get; set; }
            self.config = config;
            #public Renderer renderer { get; set; }
            self.renderer = renderer;
            self.trackingParams = trackingParams;


class YoutubeRoot(object):
    def __init__(self, assets, attrs, args):
        self.assets = assets;
        self.attrs = attrs;
        self.args = args;

def Test():
  youtubeStr = get("https://www.youtube.com/watch?v=2hafAgIlR1Y");
  baseYoutube = youtubeStr.text.encode("utf-8");
  scripts = baseYoutube.split("ytplayer.config =");
  config = scripts[1].split(";ytplayer.load =")[0];
  
  jsonString = YoutubeRoot(**json.loads(config.decode('utf-8')));
  print(jsonString.args["player_response"]);
  root = PlayerResponse(**json.loads(jsonString.args["player_response"]));
  print(root);

class pageInfo(object):
 def __init__(self, totalResults:str, resultsPerPage:str):
  self.totalResults = totalResults;
  self.resultsPerPage = resultsPerPage;

class Item(object):
 def __init__(self, kind:str):
  self.kind = kind;

class videos(object):
 def __init__(self, kind:str, etag:str, nextPageToken:str, pageInfo:List[
pageInfo], items:List[Item]):
  self.kind = kind;
  self.etag = etag;
  self.items = items;

class YoutubeView:
 @staticmethod
 def getVideoList():
  retHttp = "";
  retHttp = "<Table id='YoutubeTable' border='1'>";
  for (videoItem) in YoutubeView.getYoutubeVideos():
   retHttp +="<tr>"
   retHttp +="<td><img src=\"" + videoItem["snippet"]["thumbnails"]["default"]["url"] + "\"/></td>";
   retHttp +="<td>" + videoItem["id"] + "</td>";
   retHttp +="<td><a href=Play\?youtube="+ osDefine.Base64Encoding(videoItem["id"]) + ">" + videoItem['snippet']['title'] + "</td>"
   


   retHttp +="</tr>";
  retHttp +="</table>";
  return retHttp;

 @staticmethod
 def getYoutubeVideos():
  searchUrl = "https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&part=snippet&key=AIzaSyBdo9wdVW-g0b57kN4rrATTY7PHNs8ytR8&regionCode=kr";

  downloadString = get(searchUrl);
  decoded_videos = videos(**json.loads(downloadString.content.decode('utf-8')));
  return decoded_videos.items;


