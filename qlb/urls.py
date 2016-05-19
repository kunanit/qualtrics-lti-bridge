from django.conf.urls import patterns, url


urlpatterns = patterns('',

    url(r'^$', 'qlb.views.index', name='index'),
    url(r'^tool_config$', 'qlb.views.tool_config', name='tool_config'),
    url(r'^quiz_list$', 'qlb.views.quiz_list', name='quiz_list'),
    url(r'^select_or_create_quiz$', 'qlb.views.select_or_create_quiz', name='select_or_create_quiz'),
    url(r'^create_quiz$', 'qlb.views.create_quiz', name='create_quiz'),
    url(r'^create_qualtrics_quiz_from_url$', 'qlb.views.create_qualtrics_quiz_from_url', name='create_qualtrics_quiz_from_url'),
    url(r'^create_quiz_from_submission$', 'qlb.views.create_quiz_from_submission', name='create_quiz_from_submission'),
	url(r'^embed_quiz/(?P<quiz_id>[0-9]+)$', 'qlb.views.embed_quiz', name='embed_quiz'),
	url(r'^launch_quiz/(?P<quiz_id>[0-9]+)$', 'qlb.views.launch_quiz', name='launch_quiz'),
    # url(r'^manage_quiz/(?P<quiz_id>[0-9]+)$', 'qlb.views.manage_quiz', name='manage_quiz'),
    url(r'^modify_quiz/(?P<quiz_id>[0-9]+)$', 'qlb.views.modify_quiz', name='modify_quiz'),
    # url(r'^end_of_quiz/(?P<quiz_id>[0-9]+)$', 'qlb.views.end_of_quiz', name='end_of_quiz'),
    url(r'^end_of_quiz$', 'qlb.views.end_of_quiz', name='end_of_quiz'),
    url(r'^display_quiz_question/(?P<quiz_id>[0-9]+)$', 'qlb.views.display_quiz_question', name='display_quiz_question'),
	url(r'^display_quiz_explanation/(?P<explanation_id>[0-9]+)$', 'qlb.views.display_quiz_explanation', name='display_quiz_explanation'),

)