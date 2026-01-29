---
name: building-native-ui
description: Expo App development best practices for building native mobile interfaces. Use when developing React Native/Expo applications, implementing mobile UI patterns, optimizing performance, and creating production-grade mobile experiences.
---

# Building Native UI - Expo App Development

This skill covers best practices for building native mobile applications with Expo and React Native.

## Core Principles

### 1. Platform-Native Feel
```javascript
// Use platform-specific components
import { Platform, StyleSheet } from 'react-native'

const styles = StyleSheet.create({
  container: {
    // Platform-specific values
    padding: Platform.select({
      ios: 20,
      android: 16
    })
  }
})

// Use native components when possible
import { Switch } from 'react-native' // Native switch vs custom
```

### 2. Responsive Layouts
```javascript
import { useWindowDimensions } from 'react-native'

function ResponsiveComponent() {
  const { width, height } = useWindowDimensions()

  // Adjust layout based on screen size
  const isTablet = width > 768

  return (
    <View style={{
      flexDirection: isTablet ? 'row' : 'column'
    }}>
      {/* Content */}
    </View>
  )
}
```

### 3. Safe Area Handling
```javascript
import { useSafeAreaInsets } from 'react-native-safe-area-context'

function ScreenWithSafeArea() {
  const insets = useSafeAreaInsets()

  return (
    <View style={{
      paddingTop: insets.top,
      paddingBottom: insets.bottom,
      paddingLeft: insets.left,
      paddingRight: insets.right
    }}>
      {/* Content */}
    </View>
  )
}
```

## Navigation

### React Navigation Setup
```javascript
// AppNavigator.js
import { NavigationContainer } from '@react-navigation/native'
import { createStackNavigator } from '@react-navigation/stack'

const Stack = createStackNavigator()

function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen
          name="Details"
          component={DetailsScreen}
          options={{
            headerTitle: 'Details',
            headerStyle: { elevation: 0 }
          }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  )
}
```

### Bottom Tabs (Main Navigation)
```javascript
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs'

const Tab = createBottomTabNavigator()

function MainTabs() {
  return (
    <Tab.Navigator
      screenOptions={{
        tabBarActiveTintColor: '#007AFF',
        tabBarInactiveTintColor: '#8E8E93',
        headerShown: false
      }}
    >
      <Tab.Screen
        name="Home"
        component={HomeScreen}
        options={{
          tabBarIcon: ({ color }) => (
            <Ionicons name="home" color={color} size={24} />
          )
        }}
      />
      <Tab.Screen name="Profile" component={ProfileScreen} />
    </Tab.Navigator>
  )
}
```

## Component Patterns

### Screen Template
```javascript
import React from 'react'
import {
  View,
  Text,
  StyleSheet,
  ActivityIndicator,
  ScrollView
} from 'react-native'
import { useSafeAreaInsets } from 'react-native-safe-area-context'

function ProfileScreen({ route, navigation }) {
  const insets = useSafeAreaInsets()
  const [loading, setLoading] = React.useState(true)
  const [data, setData] = React.useState(null)

  React.useEffect(() => {
    fetchData()
  }, [])

  const fetchData = async () => {
    try {
      const response = await fetch('/api/profile')
      const json = await response.json()
      setData(json)
    } catch (error) {
      console.error('Error fetching profile:', error)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <View style={[styles.container, styles.centered]}>
        <ActivityIndicator size="large" />
      </View>
    )
  }

  return (
    <ScrollView
      style={styles.container}
      contentContainerStyle={{ paddingTop: insets.top }}
    >
      <Text style={styles.title}>Profile</Text>
      {/* Content */}
    </ScrollView>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFFFFF'
  },
  centered: {
    justifyContent: 'center',
    alignItems: 'center'
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#000000'
  }
})

export default ProfileScreen
```

### List Performance
```javascript
import { FlatList } from 'react-native'

function OptimizedList({ data }) {
  const renderItem = ({ item }) => (
    <ListItem item={item} />
  )

  const keyExtractor = (item) => item.id

  return (
    <FlatList
      data={data}
      renderItem={renderItem}
      keyExtractor={keyExtractor}
      removeClippedSubviews={true}
      maxToRenderPerBatch={10}
      windowSize={5}
      initialNumToRender={10}
    />
  )
}
```

## Best Practices

### 1. TypeScript Usage
```typescript
import type { NativeStackNavigationProp } from '@react-navigation/native-stack'

type RootStackParamList = {
  Home: undefined
  Details: { itemId: string }
}

type DetailsScreenNavigationProp = NativeStackNavigationProp<
  RootStackParamList,
  'Details'
>

type Props = {
  navigation: DetailsScreenNavigationProp
  route: RouteProp<RootStackParamList, 'Details'>
}
```

### 2. Error Boundaries
```javascript
class ErrorBoundary extends React.Component {
  state = { hasError: false }

  static getDerivedStateFromError(error) {
    return { hasError: true }
  }

  render() {
    if (this.state.hasError) {
      return <ErrorScreen />
    }
    return this.props.children
  }
}
```

### 3. Performance Optimization
- Use `React.memo` for expensive components
- Avoid anonymous functions in render
- Use `useCallback` and `useMemo` appropriately
- Optimize images with proper sizing
- Use `FastImage` for network images

### 4. Platform-Specific Code
```javascript
const Component = Platform.select({
  ios: () => require('./IOSComponent').default,
  android: () => require('./AndroidComponent').default
})()
```

## Common Pitfalls

❌ Don't do this:
```javascript
// Inline functions in render (causes re-renders)
<TouchableOpacity onPress={() => console.log('pressed')}>

// Neglecting safe areas
<View style={{ flex: 1 }}>
  {/* Content under notch/status bar */}
</View>

// Not handling different screen sizes
<View style={{ width: 300 }}>
  {/* Fixed width doesn't scale */}
</View>
```

✅ Do this instead:
```javascript
// Stable function references
const handlePress = useCallback(() => {
  console.log('pressed')
}, [])

<TouchableOpacity onPress={handlePress}>

// Safe areas handled
<SafeAreaProvider>
  <SafeAreaView edges={['top', 'left', 'right']}>
    {/* Content */}
  </SafeAreaView>
</SafeAreaProvider>

// Responsive sizing
<View style={{ width: Dimensions.get('window').width * 0.9 }}>
  {/* 90% of screen width */}
</View>
```

## Testing

```javascript
import { render, fireEvent } from '@testing-library/react-native'

test('navigates to details on button press', () => {
  const { getByText } = render(<HomeScreen />)
  fireEvent.press(getByText('Go to Details'))
  expect(navigation.navigate).toHaveBeenCalledWith('Details')
})
```

## Build & Deploy

```bash
# Development
expo start

# iOS simulator
expo start --ios

# Android emulator
expo start --android

# Build for production
eas build --platform ios
eas build --platform android

# Submit to stores
eas submit --platform ios
eas submit --platform android
```
