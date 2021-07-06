<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    xmlns:p="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"
    version="1.0">
    <xsl:output indent="yes"/>
    <xsl:template match="p:Page">
        <xsl:copy>
          <xsl:apply-templates select="@*"/>
          <p:TextRegion id="region_textline">
              <xsl:apply-templates select="./p:TextRegion/p:TextLine[not(contains(@custom, 'Drop'))]"/>
          </p:TextRegion>
        </xsl:copy>
    </xsl:template>
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>