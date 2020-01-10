. ./locations.include
sh make.product.img.sh
sh make.updates.img.sh
revisor --cli --install-dvd --yes --model=${RELEASE}${VERSIONMAJOR}-$ARCH-updates --kickstart=/etc/revisor/${RELEASE_UPPER}${VERSIONMAJOR}/ks/${RELEASE}${VERSIONMAJOR}.install.dvd.$ARCH.ks
STATUS=$?
if [ ${STATUS} -gt 0 ] ; then
   echo "revisor exited with a status of $STATUS "
   exit $STATUS
fi
echo "Created ISO in $RESULT_DIR_ISO"
