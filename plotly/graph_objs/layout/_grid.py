from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Grid(BaseLayoutHierarchyType):

    # columns
    # -------
    @property
    def columns(self):
        """
        The number of columns in the grid. If you provide a 2D
        `subplots` array, the length of its longest row is used as the
        default. If you give an `xaxes` array, its length is used as
        the default. But it's also possible to have a different length,
        if you want to leave a row at the end for non-cartesian
        subplots.
    
        The 'columns' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [1, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['columns']

    @columns.setter
    def columns(self, val):
        self['columns'] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of plotly.graph_objs.layout.grid.Domain
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
                x
                    Sets the horizontal domain of this grid subplot
                    (in plot fraction). The first and last cells
                    end exactly at the domain edges, with no grout
                    around the edges.
                y
                    Sets the vertical domain of this grid subplot
                    (in plot fraction). The first and last cells
                    end exactly at the domain edges, with no grout
                    around the edges.

        Returns
        -------
        plotly.graph_objs.layout.grid.Domain
        """
        return self['domain']

    @domain.setter
    def domain(self, val):
        self['domain'] = val

    # pattern
    # -------
    @property
    def pattern(self):
        """
        If no `subplots`, `xaxes`, or `yaxes` are given but we do have
        `rows` and `columns`, we can generate defaults using
        consecutive axis IDs, in two ways: *coupled* gives one x axis
        per column and one y axis per row. *independent* uses a new xy
        pair for each cell, left-to-right across each row then
        iterating rows according to `roworder`.
    
        The 'pattern' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['independent', 'coupled']

        Returns
        -------
        Any
        """
        return self['pattern']

    @pattern.setter
    def pattern(self, val):
        self['pattern'] = val

    # roworder
    # --------
    @property
    def roworder(self):
        """
        Is the first row the top or the bottom? Note that columns are
        always enumerated from left to right.
    
        The 'roworder' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top to bottom', 'bottom to top']

        Returns
        -------
        Any
        """
        return self['roworder']

    @roworder.setter
    def roworder(self, val):
        self['roworder'] = val

    # rows
    # ----
    @property
    def rows(self):
        """
        The number of rows in the grid. If you provide a 2D `subplots`
        array or a `yaxes` array, its length is used as the default.
        But it's also possible to have a different length, if you want
        to leave a row at the end for non-cartesian subplots.
    
        The 'rows' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [1, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['rows']

    @rows.setter
    def rows(self, val):
        self['rows'] = val

    # subplots
    # --------
    @property
    def subplots(self):
        """
        Used for freeform grids, where some axes may be shared across
        subplots but others are not. Each entry should be a cartesian
        subplot id, like *xy* or *x3y2*, or ** to leave that cell
        empty. You may reuse x axes within the same column, and y axes
        within the same row. Non-cartesian subplots and traces that
        support `domain` can place themselves in this grid separately
        using the `gridcell` attribute.
    
        The 'subplots' property is an info array that may be specified as a
        list or tuple of up to 1 elements where:
    
    (0) The 'subplots[0]' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        list
        """
        return self['subplots']

    @subplots.setter
    def subplots(self, val):
        self['subplots'] = val

    # xaxes
    # -----
    @property
    def xaxes(self):
        """
        Used with `yaxes` when the x and y axes are shared across
        columns and rows. Each entry should be an x axis id like *x*,
        *x2*, etc., or ** to not put an x axis in that column. Entries
        other than ** must be unique. Ignored if `subplots` is present.
        If missing but `yaxes` is present, will generate consecutive
        IDs.
    
        The 'xaxes' property is an info array that may be specified as a
        list or tuple of up to 1 elements where:
    
    (0) The 'xaxes[0]' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        list
        """
        return self['xaxes']

    @xaxes.setter
    def xaxes(self, val):
        self['xaxes'] = val

    # xgap
    # ----
    @property
    def xgap(self):
        """
        Horizontal space between grid cells, expressed as a fraction of
        the total width available to one cell. Defaults to 0.1 for
        coupled-axes grids and 0.2 for independent grids.
    
        The 'xgap' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['xgap']

    @xgap.setter
    def xgap(self, val):
        self['xgap'] = val

    # xside
    # -----
    @property
    def xside(self):
        """
        Sets where the x axis labels and titles go. *bottom* means the
        very bottom of the grid. *bottom plot* is the lowest plot that
        each x axis is used in. *top* and *top plot* are similar.
    
        The 'xside' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['bottom', 'bottom plot', 'top plot', 'top']

        Returns
        -------
        Any
        """
        return self['xside']

    @xside.setter
    def xside(self, val):
        self['xside'] = val

    # yaxes
    # -----
    @property
    def yaxes(self):
        """
        Used with `yaxes` when the x and y axes are shared across
        columns and rows. Each entry should be an y axis id like *y*,
        *y2*, etc., or ** to not put a y axis in that row. Entries
        other than ** must be unique. Ignored if `subplots` is present.
        If missing but `xaxes` is present, will generate consecutive
        IDs.
    
        The 'yaxes' property is an info array that may be specified as a
        list or tuple of up to 1 elements where:
    
    (0) The 'yaxes[0]' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['']
          - A string that matches one of the following regular expressions:
                ['^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        list
        """
        return self['yaxes']

    @yaxes.setter
    def yaxes(self, val):
        self['yaxes'] = val

    # ygap
    # ----
    @property
    def ygap(self):
        """
        Vertical space between grid cells, expressed as a fraction of
        the total height available to one cell. Defaults to 0.1 for
        coupled-axes grids and 0.3 for independent grids.
    
        The 'ygap' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['ygap']

    @ygap.setter
    def ygap(self, val):
        self['ygap'] = val

    # yside
    # -----
    @property
    def yside(self):
        """
        Sets where the y axis labels and titles go. *left* means the
        very left edge of the grid. *left plot* is the leftmost plot
        that each y axis is used in. *right* and *right plot* are
        similar.
    
        The 'yside' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'left plot', 'right plot', 'right']

        Returns
        -------
        Any
        """
        return self['yside']

    @yside.setter
    def yside(self, val):
        self['yside'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        columns
            The number of columns in the grid. If you provide a 2D
            `subplots` array, the length of its longest row is used
            as the default. If you give an `xaxes` array, its
            length is used as the default. But it's also possible
            to have a different length, if you want to leave a row
            at the end for non-cartesian subplots.
        domain
            plotly.graph_objs.layout.grid.Domain instance or dict
            with compatible properties
        pattern
            If no `subplots`, `xaxes`, or `yaxes` are given but we
            do have `rows` and `columns`, we can generate defaults
            using consecutive axis IDs, in two ways: *coupled*
            gives one x axis per column and one y axis per row.
            *independent* uses a new xy pair for each cell, left-
            to-right across each row then iterating rows according
            to `roworder`.
        roworder
            Is the first row the top or the bottom? Note that
            columns are always enumerated from left to right.
        rows
            The number of rows in the grid. If you provide a 2D
            `subplots` array or a `yaxes` array, its length is used
            as the default. But it's also possible to have a
            different length, if you want to leave a row at the end
            for non-cartesian subplots.
        subplots
            Used for freeform grids, where some axes may be shared
            across subplots but others are not. Each entry should
            be a cartesian subplot id, like *xy* or *x3y2*, or **
            to leave that cell empty. You may reuse x axes within
            the same column, and y axes within the same row. Non-
            cartesian subplots and traces that support `domain` can
            place themselves in this grid separately using the
            `gridcell` attribute.
        xaxes
            Used with `yaxes` when the x and y axes are shared
            across columns and rows. Each entry should be an x axis
            id like *x*, *x2*, etc., or ** to not put an x axis in
            that column. Entries other than ** must be unique.
            Ignored if `subplots` is present. If missing but
            `yaxes` is present, will generate consecutive IDs.
        xgap
            Horizontal space between grid cells, expressed as a
            fraction of the total width available to one cell.
            Defaults to 0.1 for coupled-axes grids and 0.2 for
            independent grids.
        xside
            Sets where the x axis labels and titles go. *bottom*
            means the very bottom of the grid. *bottom plot* is the
            lowest plot that each x axis is used in. *top* and *top
            plot* are similar.
        yaxes
            Used with `yaxes` when the x and y axes are shared
            across columns and rows. Each entry should be an y axis
            id like *y*, *y2*, etc., or ** to not put a y axis in
            that row. Entries other than ** must be unique. Ignored
            if `subplots` is present. If missing but `xaxes` is
            present, will generate consecutive IDs.
        ygap
            Vertical space between grid cells, expressed as a
            fraction of the total height available to one cell.
            Defaults to 0.1 for coupled-axes grids and 0.3 for
            independent grids.
        yside
            Sets where the y axis labels and titles go. *left*
            means the very left edge of the grid. *left plot* is
            the leftmost plot that each y axis is used in. *right*
            and *right plot* are similar.
        """

    def __init__(
        self,
        arg=None,
        columns=None,
        domain=None,
        pattern=None,
        roworder=None,
        rows=None,
        subplots=None,
        xaxes=None,
        xgap=None,
        xside=None,
        yaxes=None,
        ygap=None,
        yside=None,
        **kwargs
    ):
        """
        Construct a new Grid object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Grid
        columns
            The number of columns in the grid. If you provide a 2D
            `subplots` array, the length of its longest row is used
            as the default. If you give an `xaxes` array, its
            length is used as the default. But it's also possible
            to have a different length, if you want to leave a row
            at the end for non-cartesian subplots.
        domain
            plotly.graph_objs.layout.grid.Domain instance or dict
            with compatible properties
        pattern
            If no `subplots`, `xaxes`, or `yaxes` are given but we
            do have `rows` and `columns`, we can generate defaults
            using consecutive axis IDs, in two ways: *coupled*
            gives one x axis per column and one y axis per row.
            *independent* uses a new xy pair for each cell, left-
            to-right across each row then iterating rows according
            to `roworder`.
        roworder
            Is the first row the top or the bottom? Note that
            columns are always enumerated from left to right.
        rows
            The number of rows in the grid. If you provide a 2D
            `subplots` array or a `yaxes` array, its length is used
            as the default. But it's also possible to have a
            different length, if you want to leave a row at the end
            for non-cartesian subplots.
        subplots
            Used for freeform grids, where some axes may be shared
            across subplots but others are not. Each entry should
            be a cartesian subplot id, like *xy* or *x3y2*, or **
            to leave that cell empty. You may reuse x axes within
            the same column, and y axes within the same row. Non-
            cartesian subplots and traces that support `domain` can
            place themselves in this grid separately using the
            `gridcell` attribute.
        xaxes
            Used with `yaxes` when the x and y axes are shared
            across columns and rows. Each entry should be an x axis
            id like *x*, *x2*, etc., or ** to not put an x axis in
            that column. Entries other than ** must be unique.
            Ignored if `subplots` is present. If missing but
            `yaxes` is present, will generate consecutive IDs.
        xgap
            Horizontal space between grid cells, expressed as a
            fraction of the total width available to one cell.
            Defaults to 0.1 for coupled-axes grids and 0.2 for
            independent grids.
        xside
            Sets where the x axis labels and titles go. *bottom*
            means the very bottom of the grid. *bottom plot* is the
            lowest plot that each x axis is used in. *top* and *top
            plot* are similar.
        yaxes
            Used with `yaxes` when the x and y axes are shared
            across columns and rows. Each entry should be an y axis
            id like *y*, *y2*, etc., or ** to not put a y axis in
            that row. Entries other than ** must be unique. Ignored
            if `subplots` is present. If missing but `xaxes` is
            present, will generate consecutive IDs.
        ygap
            Vertical space between grid cells, expressed as a
            fraction of the total height available to one cell.
            Defaults to 0.1 for coupled-axes grids and 0.3 for
            independent grids.
        yside
            Sets where the y axis labels and titles go. *left*
            means the very left edge of the grid. *left plot* is
            the leftmost plot that each y axis is used in. *right*
            and *right plot* are similar.

        Returns
        -------
        Grid
        """
        super(Grid, self).__init__('grid')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.Grid 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Grid"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout import (grid as v_grid)

        # Initialize validators
        # ---------------------
        self._validators['columns'] = v_grid.ColumnsValidator()
        self._validators['domain'] = v_grid.DomainValidator()
        self._validators['pattern'] = v_grid.PatternValidator()
        self._validators['roworder'] = v_grid.RoworderValidator()
        self._validators['rows'] = v_grid.RowsValidator()
        self._validators['subplots'] = v_grid.SubplotsValidator()
        self._validators['xaxes'] = v_grid.XaxesValidator()
        self._validators['xgap'] = v_grid.XgapValidator()
        self._validators['xside'] = v_grid.XsideValidator()
        self._validators['yaxes'] = v_grid.YaxesValidator()
        self._validators['ygap'] = v_grid.YgapValidator()
        self._validators['yside'] = v_grid.YsideValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('columns', None)
        self.columns = columns if columns is not None else v
        v = arg.pop('domain', None)
        self.domain = domain if domain is not None else v
        v = arg.pop('pattern', None)
        self.pattern = pattern if pattern is not None else v
        v = arg.pop('roworder', None)
        self.roworder = roworder if roworder is not None else v
        v = arg.pop('rows', None)
        self.rows = rows if rows is not None else v
        v = arg.pop('subplots', None)
        self.subplots = subplots if subplots is not None else v
        v = arg.pop('xaxes', None)
        self.xaxes = xaxes if xaxes is not None else v
        v = arg.pop('xgap', None)
        self.xgap = xgap if xgap is not None else v
        v = arg.pop('xside', None)
        self.xside = xside if xside is not None else v
        v = arg.pop('yaxes', None)
        self.yaxes = yaxes if yaxes is not None else v
        v = arg.pop('ygap', None)
        self.ygap = ygap if ygap is not None else v
        v = arg.pop('yside', None)
        self.yside = yside if yside is not None else v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
