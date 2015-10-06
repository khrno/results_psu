<?php $year = isset($_GET['year']) ? $_GET['year'] : "2012"; ?>
    <html xml:lang="en" lang="en"
        xmlns="http://www.w3.org/1999/xhtml"
        xmlns:ex="http://simile.mit.edu/2006/11/exhibit#">
    <head>
        <title>PSU Resultados <?php echo $year;?></title>

        <link href="Establecimiento_PSU_anio_<?php echo $year;?>.js" type="application/json" rel="exhibit/data" />

        <script src="http://api.simile-widgets.org/exhibit/2.2.0/exhibit-api.js"
            type="text/javascript"></script>

		<script src="http://api.simile-widgets.org/exhibit/2.2.0/extensions/map/map-extension.js?gmapkey=ABQIAAAAiL-7JbUtR41RBZ1sHwon9xRWebTKG99VgVQt5nZo7xeerl1ygBR-JFpQwc4E9KGyiVGLrfZ-tM9oCQ" type="text/javascript" charset="utf-8"></script>
		<link rel="stylesheet" href="junar.css" type="text/css" />

    </head> 
    <body>
    	<div id="main-content">

    	<div style="text-align: center; margin-bottom: 3em;">
            <style>
                li {
                    display: inline;
                }
            </style>
            <ul>
            	<li><a href="?year=2006">2006</a></li>&nbsp;&nbsp;&nbsp;
                <li><a href="?year=2007">2007</a></li>&nbsp;&nbsp;&nbsp;
                <li><a href="?year=2008">2008</a></li>&nbsp;&nbsp;&nbsp;
                <li><a href="?year=2009">2009</a></li>&nbsp;&nbsp;&nbsp;
                <li><a href="?year=2010">2010</a></li>&nbsp;&nbsp;&nbsp;
                <li><a href="?year=2011">2011</a></li>&nbsp;&nbsp;&nbsp;
                <li><a href="?year=2012">2012</a></li>
            </ul>
        </div>

    	<center><h1>Resultados PSU <?php echo $year;?></h1></center><br/>
    	
    	<div class="info">Los datos fueron extra&iacute;dos y procesados desde <a href="http://datos.gob.cl" target="_blank">http://datos.gob.cl</a> </div>
    	<div id="location-facets">
    		<div id="region-facet" ex:role="facet" ex:expression=".region" ex:facetLabel="Region"></div>
			<div id="comuna-facet" ex:role="facet" ex:expression=".comuna" ex:facetLabel="Comuna"></div>
			<div id="dependencia-facet" ex:role="facet" ex:expression=".dependencia" ex:facetLabel="Dependencia"></div>
    	</div>
    	<div style="clear:both"></div>
		<div id="map">
		<div ex:role="view"
			ex:viewClass="Map"
			ex:latlng=".addressLatLng"
			ex:iconFit="none"
			ex:shape="square"
			ex:shapeWidth="30"
			ex:shapeHeight="25"
			ex:mapHeight="600"
			ex:zoom="8"
			ex:center="-34.17794211,-70.73984195">
		    <div ex:role="lens" style="display: none;" class="map-lens">
		        <div><b ex:content=".label"></b>
		        <span>
		        	Matematica: <b ex:content=".matematicas"></b>
		        	Lenguaje: <b ex:content=".lenguaje"></b>
		        	Nem: <b ex:content=".nem"></b>
		        </span></div>
		    </div>
		</div>
		</div>
		<div id="facet">
<!-- 			<div ex:role="facet" ex:facetClass="TextSearch"></div> -->
			<div ex:role="facet" ex:facetClass="NumericRange" ex:expression=".matematicas"  ex:interval="100"></div>
			<div ex:role="facet" ex:facetClass="NumericRange" ex:expression=".lenguaje"  ex:interval="100"></div>
			<div ex:role="facet" ex:facetClass="NumericRange" ex:expression=".nem"  ex:interval="100"></div>
              
		</div>
		<div style="clear:both;"></div>
		</div>
    </body>
    </html>