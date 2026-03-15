#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import math
import cv2
import torch
import pygame

# Initialize YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
inputPath = os.getcwd() + "/test_images/"
outputPath = os.getcwd() + "/output_images/"
os.makedirs(outputPath, exist_ok=True)  # Ensure output directory exists

# Default signal times
defaultGreen = 20
defaultYellow = 5
defaultMinimum = 10
defaultMaximum = 60


# In[ ]:


## Average times for vehicles to pass the intersection
carTime = 2
busTime = 2.5
truckTime = 2.5
motorcycleTime = 1.5
bicycleTime = 1
noOfLanes = 2

allowed_classes = {"car", "bus", "motorcycle", "truck", "bicycle"}


# In[ ]:


pygame.init()
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("AI Traffic flow System")
font = pygame.font.SysFont(None, 30)


# In[ ]:


def detectVehicles(filename):
    vehicle_counts = {vehicle: 0 for vehicle in allowed_classes}
    img = cv2.imread(inputPath + filename, cv2.IMREAD_COLOR)
    results = model(inputPath + filename)

    result_labels = results.pandas().xyxy[0]
    for _, vehicle in result_labels.iterrows():
        label = vehicle['name']
        if label in allowed_classes:
            vehicle_counts[label] += 1
            x_min, y_min, x_max, y_max = int(vehicle['xmin']), int(vehicle['ymin']), int(vehicle['xmax']), int(vehicle['ymax'])
            cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            cv2.putText(img, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    output_file = os.path.join(outputPath, filename)
    cv2.imwrite(output_file, img)
    return vehicle_counts, output_file


# In[ ]:


def calculateGreenTime(vehicle_counts):
    """Calculate green time based on vehicle counts for each lane."""
    noOfCars = vehicle_counts.get("car", 0)
    noOfMotorcycle = vehicle_counts.get("motorcycle", 0)
    noOfBicycle = vehicle_counts.get("bicycle", 0)
    noOfBuses = vehicle_counts.get("bus", 0)
    noOfTrucks = vehicle_counts.get("truck", 0)

    greenTime = math.ceil(((noOfCars * carTime) + (noOfBicycle * bicycleTime) +
                           (noOfBuses * busTime) + (noOfTrucks * truckTime) +
                           (noOfMotorcycle * motorcycleTime)) / (noOfLanes + 1))
    return max(min(greenTime, defaultMaximum), defaultMinimum)

def calculateRedTime(current_lane_index, green_times):
    """Calculate red time for a lane based on the green times of other lanes."""
    if current_lane_index == 0:
        return 0  # First lane starts with red time 0
    red_time = sum(green_times[:current_lane_index]) + (defaultYellow * current_lane_index)
    return red_time


# In[ ]:


def display_text(text, x, y, color=(255, 255, 255)):
    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, color)
    window.blit(text_surface, (x, y))


# In[ ]:


def main():
    start = False
    image_files = sorted([f for f in os.listdir(inputPath) if f.endswith((".jpg", ".jpeg"))])
    clock = pygame.time.Clock()
    green_times = []

    # calculate green times for each lane
    for image_file in image_files:
        vehicle_counts, _ = detectVehicles(image_file)
        green_time = calculateGreenTime(vehicle_counts)
        green_times.append(green_time)

    lane_index = 0
    start_time = pygame.time.get_ticks()  # Start timer
    all_red_times = [calculateRedTime(i, green_times) for i in range(len(green_times))]
    completed = False

    # GUI main loop
    while True:
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 300 <= event.pos[0] <= 500 and 250 <= event.pos[1] <= 300:
                    start = True  # Start button clicked

        if not start:
            pygame.draw.rect(window, (0, 128, 0), (300, 250, 200, 50))
            start_text = font.render("Start", True, (255, 255, 255))
            window.blit(start_text, (370, 260))
        elif not completed:
            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - start_time) / 1000  # seconds

            if elapsed_time >= green_times[lane_index] + defaultYellow:
                lane_index += 1
                if lane_index >= len(image_files):
                    completed = True
                    completion_time = pygame.time.get_ticks()
                else:
                    start_time = current_time

            if not completed:
                image_file = image_files[lane_index]
                vehicle_counts, output_file = detectVehicles(image_file)
                green_time = green_times[lane_index]
                red_time = all_red_times[lane_index]

                detected_img = pygame.image.load(output_file)
                detected_img = pygame.transform.scale(detected_img, (500, 400))
                window.blit(detected_img, (150, 80))

                display_text(f"Vehicle counts for {image_file}: {vehicle_counts}", 20, 500)
                display_text(f"Green time: {green_time} seconds", 20, 530)
                display_text(f"Red time: {red_time} seconds", 20, 560)

                remaining_time = max(0, green_time - elapsed_time)
                display_text(f"Remaining time: {int(remaining_time)}s", window_width - 200, 20, (255, 255, 0))

        if completed:
            display_text("Process Completed", window_width // 2 - 100, window_height // 2, (0, 255, 0))
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.quit()
            return

        pygame.display.update()
        clock.tick(30)


# In[ ]:


main()

