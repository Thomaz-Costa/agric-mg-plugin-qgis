# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SelectAgric
                                 A QGIS plugin
 Suporte a decisão para seleção de áreas agricolas
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-08
        copyright            : (C) 2024 by Thomaz Costa
        email                : thomaz.costa@embrapa.br
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SelectAgric class from file SelectAgric.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .select_agric import SelectAgric
    return SelectAgric(iface)
