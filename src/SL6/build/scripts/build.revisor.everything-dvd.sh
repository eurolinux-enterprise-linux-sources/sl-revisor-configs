. ./locations.include
sh make.product.img.sh
sh make.updates.img.sh
revisor --config ${RELEASE}${VERSIONMAJOR}-everything.conf --yes --cli --install-dvd   --model=${RELEASE}${VERSIONMAJOR}-$ARCH --kickstart=/etc/revisor/${RELEASE_UPPER}${VERSIONMAJOR}/ks/${RELEASE}${VERSIONMAJOR}.everything.ks
STATUS=$?
if [ ${STATUS} -gt 0 ] ; then
   echo "revisor exited with a status of $STATUS "
   exit $STATUS
fi
echo "Created ISO in $RESULT_DIR_ISO"
