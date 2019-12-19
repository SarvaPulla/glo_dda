from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import PersistentStoreDatabaseSetting, PersistentStoreConnectionSetting


class GloDda(TethysAppBase):
    """
    Tethys app class for Design Data Availability
    """

    name = 'Design Data Availability'
    index = 'glo_dda:home'
    icon = 'glo_dda/images/logo.jpg'
    package = 'glo_dda'
    root_url = 'glo-dda'
    color = '#16a085'
    description = 'Design Data Availability'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='glo-dda',
                controller='glo_dda.controllers.home'
            ),
            UrlMap(
                name='popup-info',
                url='glo-dda/popup-info',
                controller='glo_dda.controllers_ajax.get_popup_info'
            ),
            UrlMap(
                name='get-meta-file',
                url='glo-dda/get-meta-file',
                controller='glo_dda.controllers_ajax.get_meta_file'
            ),
            UrlMap(
                name='add-point',
                url='glo-dda/add-point',
                controller='glo_dda.controllers.add_point'
            ),
            UrlMap(
                name='delete-layer',
                url='glo-dda/delete-layer',
                controller='glo_dda.controllers.delete_layer'
            ),
            UrlMap(
                name='submit-delete-layer',
                url='glo-dda/delete-layer/submit',
                controller='glo_dda.controllers_ajax.layer_delete'
            ),
            UrlMap(
                name='add-point-ajax',
                url='glo-dda/add-point/submit',
                controller='glo_dda.controllers_ajax.point_add'
            ),
            UrlMap(
                name='approve-points',
                url='glo-dda/approve-points',
                controller='glo_dda.controllers.approve_points'
            ),
            UrlMap(
                name='approve-points_tabulator',
                url='glo-dda/approve-points/tabulator',
                controller='glo_dda.controllers_ajax.points_tabulator'
            ),
            UrlMap(
                name='update-points-ajax',
                url='glo-dda/approve-points/submit',
                controller='glo_dda.controllers_ajax.point_update'
            ),
            UrlMap(
                name='delete-points-ajax',
                url='glo-dda/approve-points/delete',
                controller='glo_dda.controllers_ajax.point_delete'
            ),
            UrlMap(
                name='add-polygon',
                url='glo-dda/add-polygon',
                controller='glo_dda.controllers.add_polygon'
            ),
            UrlMap(
                name='add-polygon-ajax',
                url='glo-dda/add-polygon/submit',
                controller='glo_dda.controllers_ajax.polygon_add'
            ),
            UrlMap(
                name='approve-polygons',
                url='glo-dda/approve-polygons',
                controller='glo_dda.controllers.approve_polygons'
            ),
            UrlMap(
                name='approve-polygons-tabulator',
                url='glo-dda/approve-polygons/tabulator',
                controller='glo_dda.controllers_ajax.polygons_tabulator'
            ),
            UrlMap(
                name='update-polygons-ajax',
                url='glo-dda/approve-polygons/submit',
                controller='glo_dda.controllers_ajax.polygon_update'
            ),
            UrlMap(
                name='delete-polygons-ajax',
                url='glo-dda/approve-polygons/delete',
                controller='glo_dda.controllers_ajax.polygon_delete'
            ),
            UrlMap(
                name='add-new-layer',
                url='glo-dda/add-new-layer',
                controller='glo_dda.controllers.add_new_layer'
            ),
            UrlMap(
                name='get-new-layer-attributes',
                url='glo-dda/add-new-layer/get-attributes',
                controller='glo_dda.controllers_ajax.get_shp_attributes'
            ),
            UrlMap(
                name='add-new-layer-ajax',
                url='glo-dda/add-new-layer/submit',
                controller='glo_dda.controllers_ajax.new_layer_add'
            ),
            UrlMap(
                name='set-layer-style',
                url='glo-dda/set-layer-style',
                controller='glo_dda.controllers.set_layer_style'
            ),
            UrlMap(
                name='set-layer-style-ajax',
                url='glo-dda/set-layer-style/submit',
                controller='glo_dda.controllers_ajax.layer_style_set'
            ),
            UrlMap(
                name='add-endpoint',
                url='glo-dda/add-endpoint',
                controller='glo_dda.controllers.add_endpoint'
            ),
            UrlMap(
                name='add-endpoint-submit',
                url='glo-dda/add-endpoint/submit',
                controller='glo_dda.controllers_ajax.endpoint_add'
            ),
            UrlMap(
                name='delete-endpoint',
                url='glo-dda/delete-endpoint',
                controller='glo_dda.controllers.delete_endpoint'
            ),
            UrlMap(
                name='delete-endpoint-submit',
                url='glo-dda/delete-endpoint/submit',
                controller='glo_dda.controllers_ajax.endpoint_delete'
            ),
            UrlMap(
                name='get-layers-info',
                url='glo-dda/api/get-layers-info',
                controller='glo_dda.api.get_layers_info'
            ),
            UrlMap(
                name='get-layers-by-county',
                url='glo-dda/api/get-layers-by-county',
                controller='glo_dda.api.get_layers_by_county'
            ),
            UrlMap(
                name='get-points-by-county',
                url='glo-dda/api/get-points-by-county',
                controller='glo_dda.api.get_points_by_county'
            ),
            UrlMap(
                name='get-polygons-by-county',
                url='glo-dda/api/get-polygons-by-county',
                controller='glo_dda.api.get_polygons_by_county'
            ),
            UrlMap(
                name='get-points-by-layer',
                url='glo-dda/api/get-points-by-layer',
                controller='glo_dda.api.get_points_by_layer'
            ),
            UrlMap(
                name='get-polygons-by-layer',
                url='glo-dda/api/get-polygons-by-layer',
                controller='glo_dda.api.get_polygons_by_layer'
            ),
            UrlMap(
                name='get-points-by-geometry',
                url='glo-dda/api/get-points-by-geometry',
                controller='glo_dda.api.get_points_by_geom'
            ),
            UrlMap(
                name='get-polygons-by-geometry',
                url='glo-dda/api/get-polygons-by-geometry',
                controller='glo_dda.api.get_polygons_by_geom'
            ),
            UrlMap(
                name='dowloand-layers',
                url='glo-dda/download-layers',
                controller='glo_dda.controllers_ajax.download_layers'
            ),
            UrlMap(
                name='download-interaction',
                url='glo-dda/download-interaction',
                controller='glo_dda.controllers_ajax.download_interaction'
            ),
            UrlMap(
                name='download-points-csv',
                url='glo-dda/api/download-points-csv',
                controller='glo_dda.api.download_points_csv'
            ),
            UrlMap(
                name='download-polygons-csv',
                url='glo-dda/api/download-polygons-csv',
                controller='glo_dda.api.download_polygons_csv'
            ),
            UrlMap(
                name='download-layer-csv',
                url='glo-dda/api/download-layer-csv',
                controller='glo_dda.api.download_layer_csv'
            ),
        )

        return url_maps

    def persistent_store_settings(self):
        """
        Define Persistent Store Settings.
        """
        ps_settings = (
            PersistentStoreDatabaseSetting(
                name='layers',
                description='layers database',
                initializer='glo_dda.model.init_layer_db',
                required=True,
                spatial=True
            ),
        )

        return ps_settings
