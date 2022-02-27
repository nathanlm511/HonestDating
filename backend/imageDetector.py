# import the necessary packages
import numpy as np
import argparse
import cv2

class ImageDetector():
	def __init__(self, prototxt, model):
		self.proto = prototxt
		self.model = model
		self.net = cv2.dnn.readNetFromCaffe(self.proto, self.model)
		
		self.CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
			"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
			"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
			"sofa", "train", "tvmonitor"]
		self.COLORS = np.random.uniform(0, 255, size=(len(self.CLASSES), 3))

	def detectObjects(self, image, thresh_conf=.5, debug=False):
		(h, w) = image.shape[:2]
		blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

		if debug: print("[INFO] computing object detections...")
		self.net.setInput(blob)
		detections = self.net.forward()

		# detected_objects = {"background":0, "aeroplane":0, "bicycle":0, "bird":0, "boat":0,
		# 	"bottle":0, "bus":0, "car":0, "cat":0, "chair":0, "cow":0, "diningtable":0,
		# 	"dog":0, "horse":0, "motorbike":0, "person":0, "pottedplant":0, "sheep":0,
		# 	"sofa":0, "train":0, "tvmonitor":0}
		detected_objects = []

		# loop over the detections
		for i in np.arange(0, detections.shape[2]):
			# extract the confidence (i.e., probability) associated with the
			# prediction
			confidence = detections[0, 0, i, 2]

			# filter out weak detections by ensuring the `confidence` is
			# greater than the minimum confidence
			if confidence > thresh_conf:
				# extract the index of the class label from the `detections`,
				# then compute the (x, y)-coordinates of the bounding box for
				# the object
				idx = int(detections[0, 0, i, 1])
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")

				# display the prediction
				label = "{}: {:.2f}%".format(self.CLASSES[idx], confidence * 100)
				if debug: print("[INFO] {}".format(label))
				cv2.rectangle(image, (startX, startY), (endX, endY), self.COLORS[idx], 2)
				y = startY - 15 if startY - 15 > 15 else startY + 15
				cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.COLORS[idx], 2)
				if self.CLASSES[idx] not in detected_objects:
					detected_objects.append(self.CLASSES[idx])
		return detected_objects